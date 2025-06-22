import pathlib

import dotenv
import asyncio
import pytest_asyncio
import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

pytest_plugins = ("pytest_asyncio",)


@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()

# @pytest.mark.asyncio
def test_eval_full_conversation():
    """에이전트의 기본 동작을 몇 가지 예제로 테스트합니다."""
    AgentEvaluator.evaluate(
        agent_module="agent_eval",
        eval_dataset_file_path_or_dir=str(
            pathlib.Path(__file__).parent / "data/conversation.test.json"
        ),
        num_runs=1,
    )

if __name__ == "__main__":
    test_eval_full_conversation()
