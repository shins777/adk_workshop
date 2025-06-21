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
    """Test the agent's basic ability on a few examples."""
    AgentEvaluator.evaluate(
        agent_module="agent_eval",
        eval_dataset_file_path_or_dir=str(
            pathlib.Path(__file__).parent / "data/conversation.test.json"
        ),
        num_runs=1,
    )

if __name__ == "__main__":
    test_eval_full_conversation()
