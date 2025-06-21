import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

load_dotenv()

def build_agent():
    """
    Creates and configures an Agent instance with Google Search tool support.

    This function loads environment variables, defines the agent's instruction template,
    and initializes the Agent with a name, model, description, instruction, and the Google Search tool.
    The agent is designed to answer user questions by performing a Google search and providing
    answers in a structured format including the question, source information, and answer.

    Returns:
        Agent: A configured Agent instance ready to process user queries.
    """

    INSTRUCTION = """
        You are an agent who provides answers to users' questions.
        When a user enters a question, you should perform a Google search(tool:google_search) for that question and provide an answer based on the results.
        When you provide an answer, you have to follow the below format exactly:

        1. Question: 
        2. Source information: 
        3. Answer: 

        Note : When answering, Must be sure to use the same language the user used when asking the question. 
        
    """

    search_agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[google_search],
        output_key = "last_turn"
    )
    return search_agent

root_agent = build_agent()
