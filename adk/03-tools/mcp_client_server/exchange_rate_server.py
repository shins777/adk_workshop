import asyncio
import json
from dotenv import load_dotenv

# MCP 서버 관련 임포트
from mcp import types as mcp_types # genai.types와의 충돌을 피하기 위해 별칭 사용
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# ADK 도구 관련 임포트
from google.adk.tools.function_tool import FunctionTool
# ADK <-> MCP 변환 유틸리티
from google.adk.tools.mcp_tool.conversion_utils import adk_to_mcp_tool_type

# --- 환경 변수 로드 (ADK 도구에서 필요할 경우) ---
load_dotenv()

mcp_svr_app = None
exchange_rate_tool = None 

#-----------------------[get_exchange_rate]-----------------------
# 환율 조회 함수 정의

def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "KRW",
    currency_date: str = "latest", )->dict:
    """
    지정한 날짜에 두 통화 간의 환율을 조회합니다.

    Frankfurter API(https://api.frankfurter.app/)를 사용하여
    환율 데이터를 가져옵니다.

    인자:
        currency_from: 기준 통화(3자리 통화 코드). 기본값은 "USD"(미국 달러).
        currency_to: 대상 통화(3자리 통화 코드). 기본값은 "KRW"(원화).
        currency_date: 환율을 조회할 날짜. 기본값은 "latest"로 최신 환율 데이터를 의미합니다.
            과거 환율은 YYYY-MM-DD 형식으로 지정할 수 있습니다.

    반환값:
        dict: 환율 정보가 담긴 딕셔너리.
            예시: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """
    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

#-----------------------[mcp_server_init]-----------------------
# MCP 서버 및 ADK 도구 초기화 함수

def mcp_server_init():
    """
    MCP 서버와 ADK 환율 도구를 초기화합니다.

    이 함수는 환율 조회를 위한 ADK FunctionTool을 생성하고 초기화 메시지를 출력합니다.
    이후 MCP 서버 인스턴스를 생성하여 MCP를 통해 도구를 노출할 수 있도록 반환합니다.

    반환값:
        tuple: MCP 서버 인스턴스와 초기화된 환율 도구가 포함된 튜플
    """

    exchange_rate_tool = FunctionTool(func=get_exchange_rate)

    print("Initializing ADK exchange rate tool...")
    print(f"ADK tool '{exchange_rate_tool.name}' initialized.")

    # --- MCP Server Setup ---
    print("Creating MCP Server instance...")
    mcp_svr_app = Server("adk-exchange-rate-mcp-server") 
    print("MCP Server instance created.")

    return mcp_svr_app, exchange_rate_tool

mcp_svr_app, exchange_rate_tool = mcp_server_init()

#-----------------------[list_tools]-----------------------

@mcp_svr_app.list_tools()
async def list_tools() -> list[mcp_types.Tool]:
    """
    사용 가능한 도구 목록을 반환하는 MCP 핸들러입니다.

    이 함수는 MCP 서버가 사용 가능한 도구 목록을 제공할 때 호출됩니다.
    ADK 도구의 정의를 MCP 도구 스키마 형식으로 변환하여 리스트로 반환합니다.
    이를 통해 클라이언트가 서버에서 노출하는 도구를 확인할 수 있습니다.

    반환값:
        list[mcp_types.Tool]: 사용 가능한 MCP 도구 스키마 리스트
    """

    print("MCP Server: Received list_tools request.")
    # ADK 도구의 정의를 MCP 형식으로 변환
    mcp_tool_schema = adk_to_mcp_tool_type(exchange_rate_tool)
    print(f"MCP Server: Advertising tool: {mcp_tool_schema.name}")
    return [mcp_tool_schema]

#-----------------------[call_tool]-----------------------
@mcp_svr_app.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
    """
    MCP에서 도구 실행 요청을 처리하는 핸들러입니다.

    이 함수는 클라이언트가 도구 실행을 요청할 때 호출됩니다.
    요청된 도구 이름이 ADK 도구와 일치하면 비동기로 실행하고,
    결과를 MCP 콘텐츠 형식으로 반환합니다. 도구가 없거나 오류가 발생하면
    MCP 형식의 에러 메시지를 반환합니다.

    인자:
        name (str): 실행할 도구 이름
        arguments (dict): 도구에 전달할 인자
    반환값:
        list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
            도구의 응답이 MCP 콘텐츠로 포맷된 리스트
    """

    print(f"MCP Server: Received call_tool request for '{name}' with args: {arguments}")

    # 요청된 도구 이름이 래핑된 ADK 도구와 일치하는지 확인
    if name == exchange_rate_tool.name:
        try:
            # ADK 도구의 run_async 메서드 실행
            # 참고: tool_context는 전체 ADK Runner 호출이 아니므로 None 사용
            adk_response = await exchange_rate_tool.run_async(
                args=arguments,
                tool_context=None, # 여기서는 ADK 컨텍스트 없음
            )
            print(f"MCP Server: ADK tool '{name}' executed successfully.")
            # ADK 도구의 응답(대개 dict)을 MCP 형식으로 변환
            # 여기서는 응답 딕셔너리를 JSON 문자열로 직렬화하여 TextContent에 담음
            # 실제 도구 출력 및 클라이언트 요구에 따라 포맷 조정 가능
            response_text = json.dumps(adk_response, indent=2)
            return [mcp_types.TextContent(type="text", text=response_text)]

        except Exception as e:
            print(f"MCP Server: Error executing ADK tool '{name}': {e}")
            # MCP 형식의 에러 메시지 반환
            # 더 견고한 MCP 에러 응답 생성 가능
            error_text = json.dumps({"error": f"Failed to execute tool '{name}': {str(e)}"})
            return [mcp_types.TextContent(type="text", text=error_text)]
    else:
        # 알 수 없는 도구 호출 처리
        print(f"MCP Server: Tool '{name}' not found.")
        error_text = json.dumps({"error": f"Tool '{name}' not implemented."})
        # 간단히 TextContent로 에러 반환
        return [mcp_types.TextContent(type="text", text=error_text)]

#-----------------------[run_server]-----------------------
async def run_server():
    """
    MCP 서버를 표준 입출력으로 실행합니다.

    이 함수는 MCP 라이브러리의 stdio_server 컨텍스트 매니저를 사용해 서버를 시작하고,
    핸드셰이크를 수행한 뒤, 메인 이벤트 루프에 진입하여 요청과 도구 실행을 처리합니다.
    MCP 서버 프로세스의 메인 진입점으로 사용됩니다.

    반환값:
        없음
    """
  
    # MCP 라이브러리의 stdio_server 컨텍스트 매니저 사용
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        print("MCP Server starting handshake...")
        await mcp_svr_app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=mcp_svr_app.name, # 위에서 정의한 서버 이름 사용
                server_version="0.1.0",
                capabilities=mcp_svr_app.get_capabilities(
                    # 서버 기능 정의 - MCP 문서 참고
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        print("MCP Server run loop finished.")


if __name__ == "__main__":
    print("Launching MCP Server exposing ADK tools...")
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\nMCP Server stopped by user.")
    except Exception as e:
        print(f"MCP Server encountered an error: {e}")
    finally:
        print("MCP Server process exiting.")
