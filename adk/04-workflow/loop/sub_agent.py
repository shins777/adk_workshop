# Copyright 2025 Forusone(forusone777@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.tools import ToolContext

load_dotenv()

RESEARCH_OUTCOME = "initial_sentence"
STATE_CRITICISM = "criticism"
COMPLETION_PHRASE = "No major issues found."

SYSTEM_INSTRUCTION = """
    When answering, Must be sure to use the same language the user used when asking the question. 
"""

#--------------------------------[exit_loop]----------------------------------

def exit_loop(tool_context: ToolContext):
    """
    Signals the loop agent to exit the current loop iteration.

    This function is intended to be called as a tool by an agent within a loop.
    It sets the 'escalate' action in the tool context to True, which instructs the
    loop agent to break out of the loop and proceed to the next step in the workflow.

    Args:
        tool_context (ToolContext): The context object containing agent and action information.

    Returns:
        dict: An empty dictionary, as no additional output is required.
    """
  
    print(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True

    return {}

#--------------------------------[research_agent]----------------------------------

research_agent = Agent(
    name = "research_agent",
    model = os.getenv("MODEL"),
    description = "An agent that answers the positive and negative aspects of a user's questions.",
    instruction = """
            You are an agent who writes positive and negative reviews on a given topic.
            When providing an answer, you should write as concisely and clearly as possible, and start by saying "Write a review.
            Note : When answering, Must be sure to use the same language the user used when asking the question. 

                """,
    output_key="RESEARCH_OUTCOME"                
)    

#--------------------------------[critic_agent]----------------------------------

critic_agent = Agent(
    name = "critic_agent",
    model = os.getenv("MODEL"),
    description = "An Agent that reviews answers to a given topic.",
    instruction = f"""
                    You are a constructive critique AI Agent that reviews answers to a given topic. 
                    Add a title of "## Answer Review" to your answers.

                    **Answers to the given topic:**
                        ```
                        {RESEARCH_OUTCOME}
                        ```

                    **Tasks:**
                        Please review your response clearly against the following criteria:

                        Provide 1-2 *clear and actionable* ways to improve the response.
                        Must include implications for our society and organization.
                        Provide specific suggestions concisely, such as: Print *only* the critique text. Document

                    ** If the answer is ok :
                    Must respond *exactly* with the phrase "{COMPLETION_PHRASE}" and do not output any other phrases or add any explanations.

                    Note : When answering, Must be sure to use the same language the user used when asking the question. 

                                
                """,
    output_key=STATE_CRITICISM,                
)   

#--------------------------------[refine_agent]----------------------------------

refine_agent = Agent(
    name = "refine_agent",
    model = os.getenv("MODEL"),
    description = "An Agent that refine answers to a given topic.",
    instruction = f"""
                    You are a constructive critique AI Agent that reviews answers to users' questions. 
                    Add a title of "## Answer Verification" to your response.

                    **Answers to a given topic:**
                        ```
                        {RESEARCH_OUTCOME}
                        ```
                    **Critique/Suggestion:**
                        {STATE_CRITICISM}

                    **Tasks:**
                        Analyze 'Criticism/Suggestion'.

                        If the critique is *exactly* "{COMPLETION_PHRASE}":
                            You must call the 'exit_loop' function. Don't output the text.
                        Otherwise (if the critique contains actionable feedback):
                            Apply the suggestion carefully to improve the 'current document'. Output *only* the polished document text.
                            Don't add descriptions. Output the polished document or call the exit_loop function.

                    Note : When answering, Must be sure to use the same language the user used when asking the question. 

                """,
    
    tools=[exit_loop],

)   

#--------------------------------[conclusion_agent]----------------------------------

conclusion_agent = Agent(
    name = "conclusion_agent",
    model = os.getenv("MODEL"),
    description = "Agent that summarizes the positive and negative aspects of a user's question",
    instruction = f"""
                    You are an agent who explains the final summary and conclusion based on the positive and negative criticisms on the given topic.
                    When answering, please refer to the current document below and the criticism/suggestion section and say "final summary" and answer.
                    
                    **Answers to a given topic:**
                    ```
                    {RESEARCH_OUTCOME}
                    ```
                    **Critique/Suggestion:**
                    {STATE_CRITICISM}

                    Note : When answering, Must be sure to use the same language the user used when asking the question. 

                """,
)