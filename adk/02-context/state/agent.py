import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

load_dotenv()

INSTRUCTION = """
    You are an agent that provides answers to user questions.
    When a user submits a question, perform a Google search (tool: google_search)
    for that question and provide an answer based on the results.
"""

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that answers user queries",
    instruction = INSTRUCTION,
    tools=[google_search],
    output_key = "last_turn"
)

