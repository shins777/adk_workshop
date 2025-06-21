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

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from a2a.utils.errors import ServerError
from a2a.types import UnsupportedOperationError

class EchoAgent:
    """
    A simple agent that echoes back the user's query in uppercase.

    The EchoAgent provides a single asynchronous method, `invoke`, which takes a string query
    and returns a formatted string with the query converted to uppercase. This class is intended
    for demonstration or testing purposes, showing how an agent can process and respond to input.

    Methods:
        invoke(query: str) -> str: Asynchronously returns the uppercase version of the input query.
    """

    async def invoke(self, query: str) -> str:
        return f"\n###  🤖 EchoAgent : {query.upper()}"

class EchoAgentExecutor(AgentExecutor):
    """
    An agent executor that delegates user queries to an EchoAgent and enqueues the response.

    The EchoAgentExecutor manages the lifecycle of an EchoAgent, handling the execution context
    and event queue. It processes user input, invokes the agent to generate a response, and
    enqueues the result as an event for downstream consumption. The executor also provides a
    cancel method that raises an error for unsupported operations.

    Methods:
        execute(context, event_queue): Processes the user query, invokes the agent, and enqueues the response.
        cancel(context, event_queue): Raises an error indicating that cancellation is not supported.
    """

    def __init__(self):
        self.agent = EchoAgent()

    async def execute(self,
                      context: RequestContext,
                      event_queue: EventQueue,) -> None:
    
        print(f"### Before invoking Agent context : {context}")
        
        # https://google-a2a.github.io/A2A/sdk/python/#a2a.server.agent_execution.RequestContext
        message = context.message
        query = context.get_user_input()

        print(f"### Message : {message}")
        print(f"### User's query : {query}")
    
        result = await self.agent.invoke(query=query)        

        print(f"### After invoking Agent result : {result}")

        # Put the result to event_eqeue to send the results to the client. 
        event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, 
                     context: RequestContext, 
                     event_queue: EventQueue) -> None:
        
        raise ServerError(error=UnsupportedOperationError())

