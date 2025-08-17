# Copyright 2025 Forusone(shins777@gmail.com)
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

from typing import AsyncGenerator
from typing_extensions import override

from google.adk.agents import LlmAgent, BaseAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext

from google.adk.events import Event
from google.adk.agents import SequentialAgent

class CriticAgent(BaseAgent):
    """
    Coordinate a multi-step critique workflow using sub-agents.

    The CriticAgent orchestrates three LlmAgent sub-agents: positive_critic_agent,
    negative_critic_agent, and review_critic_agent. It runs a positive critique,
    a negative critique, and finally the review critique, yielding events
    produced by each stage. The agent may abort the workflow early if required
    output conditions are not met (for example, if specific keywords are missing
    from the state). This enables conditional, multi-stage evaluation and review
    of user input or generated content.

    Attributes:
        positive_critic_agent (LlmAgent): Agent that produces positive criticism.
        negative_critic_agent (LlmAgent): Agent that produces negative criticism.
        review_critic_agent (LlmAgent): Agent that reviews the aggregated critiques.
        sequential_agent (SequentialAgent): Internal sequential agent used to manage the workflow.

    Methods:
        _run_async_impl(ctx): Asynchronously execute the critique workflow and yield events.
    """

    positive_critic_agent: LlmAgent
    negative_critic_agent: LlmAgent
    review_critic_agent: LlmAgent

    sequential_agent: SequentialAgent

    # model_config allows setting Pydantic configurations if needed, e.g., arbitrary_types_allowed
    model_config = {"arbitrary_types_allowed": True}

    def __init__(
        self,
        name: str,
        positive_critic_agent: LlmAgent,
        negative_critic_agent: LlmAgent,
        review_critic_agent: LlmAgent,
    ):
        sequential_agent = SequentialAgent(
            name="PostProcessing", sub_agents=[positive_critic_agent, negative_critic_agent]
        )

        sub_agents_list = [
            sequential_agent,
            review_critic_agent,
        ]

        super().__init__(
            name=name,
            positive_critic_agent=positive_critic_agent,
            negative_critic_agent=negative_critic_agent,
            review_critic_agent=review_critic_agent,
            sequential_agent=sequential_agent,
            sub_agents=sub_agents_list,
        )

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:

        """
        Execute the multi-step critique workflow asynchronously.

        This method runs the positive, negative, and review critique agents in order,
        yielding events from each step. If required output conditions are not met
        (for example, a missing keyword in the state after a step), the workflow may
        be aborted early. This supports conditional, staged evaluation and review of
        user inputs or generated content.

        Args:
            ctx (InvocationContext): The invocation context containing session and state.

        Yields:
            Event: Events produced by sub-agents during workflow execution.
        """

        #-----------[positive_critic_agent]--------------
        print(f"[{self.name}] Running positive_critic_agent...")
        async for event in self.positive_critic_agent.run_async(ctx):

            print(f"[{self.name}] Event from positive_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event  # yield an event and move on to the next step

        # Optional early-exit check for positive critic results:
        # Inspect the positive critic output and abort the workflow if required
        # keywords are missing. The example below is commented out but shows
        # how to implement conditional stopping logic.
        # if "images" not in ctx.session.state["positive_critic_output"].lower():
        #     print(f"[{self.name}] Failed to generate answer since no mention about images. Aborting workflow.")
        #     return  # Stop processing if positive critic failed

        #-----------[negative_critic_agent]--------------
        print(f"[{self.name}] Running negative_critic_agent...")
        async for event in self.negative_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from negative_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event  # yield an event and move on to the next step

        # Optional early-exit check for negative critic results:
        # If specific conditions are not met (e.g., missing keyword), abort the workflow.
        # Example (commented):
        # if "social" not in ctx.session.state["negative_critic_output"].lower():
        #     print(f"[{self.name}] Failed to generate answer since no mention about social issues. Aborting workflow.")
        #     return  # Stop processing if negative critic failed

        #-----------[review_critic_agent]--------------
        print(f"[{self.name}] Running review_critic_agent")
        async for event in self.review_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from review_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event
