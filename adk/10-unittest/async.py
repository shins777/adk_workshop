import asyncio
import time

async def fetch_data(delay: int, data: str) -> str:
    """비동기 네트워크 요청을 시뮬레이션합니다."""
    print(f"{data}를 {delay}초 동안 가져오는 중...")
    await asyncio.sleep(delay) # 일시 중지: 제어권을 이벤트 루프에 넘겨줍니다.
    print(f"{data} 가져오기 완료.")
    return f"{delay}초 후 {data}에서 온 데이터"

async def main():
    print("메인 프로그램 시작.")

    # 이 태스크들은 'await'와 이벤트 루프 덕분에 동시에 실행됩니다.
    task1 = asyncio.create_task(fetch_data(3, "API_A"))
    task2 = asyncio.create_task(fetch_data(1, "API_B"))
    task3 = asyncio.create_task(fetch_data(2, "Database_C"))

    # 각 태스크가 완료되면 결과를 얻기 위해 await합니다.
    # 이 await의 순서는 'main'이 결과를 받는 시기를 결정하지만,
    # 태스크 자체는 위에서 동시에 시작되었습니다.
    result_a = await task1
    result_b = await task2
    result_c = await task3

    print(f"결과 A: {result_a}")
    print(f"결과 B: {result_b}")
    print(f"결과 C: {result_c}")
    print("메인 프로그램 종료.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main()) # 메인 코루틴을 실행합니다.
    end_time = time.perf_counter()
    print(f"\n총 실행 시간: {end_time - start_time:.2f}초")