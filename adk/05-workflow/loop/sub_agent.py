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
from google.adk.tools import google_search

load_dotenv()

COMPLETION_PHRASE = "Overall, the answer is fine."

#--------------------------------[exit_loop]----------------------------------

def exit_loop(tool_context: ToolContext):
    """
    Signal the loop agent to exit the current iteration.

    This function is intended to be called as a tool from within a loop agent.
    It signals the loop controller to advance to the next step of the workflow by
    setting the `escalate` action flag on the provided ToolContext.

    Args:
        tool_context (ToolContext): Context object containing agent and action information.

    Returns:
        dict: An empty dictionary since no additional output is required.
    """
  
    print(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
    
    # Signal the loop agent to exit the current iteration.
    # Set the 'escalate' action flag on the tool context so the loop controller
    # can break out of the loop and continue with the next workflow stage.
    tool_context.actions.escalate = True

    return {}

#--------------------------------[research_agent]----------------------------------

# research_agent: gathers or generates initial content for the topic.
research_agent = Agent(
    name = "research_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that drafts positive and negative aspects for a given topic.",
    instruction = """
            You are an agent that writes the positive and negative aspects for a given topic.
            When providing an answer, be as concise and clear as possible, and begin with "### Research Results: "
            Note: Always respond in the same language as the user's question.

            """,
    tools=[google_search],

    output_key="research_outcome",
)

#--------------------------------[critic_agent]----------------------------------

# critic_agent: produces a concise, constructive critique of the research output.
critic_agent = Agent(
    name = "critic_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "A constructive critic AI agent that reviews an answer for a given topic.",
    instruction = f"""
                    You are a constructive critic AI agent that reviews the provided answer for a given topic.
                    Add the heading "### Answer Review" to your response.

                    **Provided answer for the topic:**
                        ```
                        {{research_outcome}}
                        ```

                    **Task:**
                        Review the answer clearly according to the following criteria:

                        - Suggest 1-2 *clear and actionable* ways to improve the response.
                        - Include implications for society and organizations where relevant.
                        - Provide concise, specific suggestions. For example: output *only* the critique text.

                    **If the answer is acceptable:**
                        Respond *exactly* with the phrase "{COMPLETION_PHRASE}" and do not output any other text or explanations.

                    Note: Always respond in the same language as the user's question.

                """,
    output_key="criticism",
)

#--------------------------------[refine_agent]----------------------------------

# refine_agent: applies critique suggestions or calls `exit_loop` when the
# critique indicates the output is satisfactory.
refine_agent = Agent(
    name = "refine_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "A constructive refinement agent that evaluates and applies critiques to improve the answer.",
    instruction = f"""
                    You are a constructive refinement agent that reviews the user's answer.
                    Add the heading "## Answer Validation" to your response.

                    **Provided answer for the topic:**
                        ```
                        {{research_outcome}}
                        ```
                    **Critique / Suggestions:**
                        ```
                        {{criticism}}
                        ```
                    **Task:**
                        Analyze the 'critique / suggestions'.

                        If the critique is *exactly* "{COMPLETION_PHRASE}":
                            Call the 'exit_loop' function. Do not output any text.
                        Otherwise (if the critique includes actionable feedback):
                            Carefully apply the suggestions to improve the 'current document'. Output *only* the improved document text.
                            Do not add explanations. Either output the improved document or call the exit_loop function.

                    Note: Always respond in the same language as the user's question.

                """,
    
    tools=[exit_loop],

)

#--------------------------------[conclusion_agent]----------------------------------

# conclusion_agent: summarizes positive and negative aspects and produces the final summary.
conclusion_agent = Agent(
    name = "conclusion_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that summarizes the positive and negative aspects of a user's query and provides a final summary.",
    instruction = f"""
                    You are an agent that explains the final summary and conclusion based on positive and negative critiques for the given topic.
                    When responding, refer to the current document and the Critique/Suggestions section below and begin your answer with "### Final Summary".
                    
                    **Provided answer for the topic:**
                    ```
                    {{research_outcome}}
                    ```
                    **Critique / Suggestions:**
                    ```
                    {{criticism}}
                    ```
                    Note: Always respond in the same language as the user's question.

                """,
)