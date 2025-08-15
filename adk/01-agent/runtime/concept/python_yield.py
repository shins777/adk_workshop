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

"""
The following describes how a sub-agent operates within an AI agent, using Python's yield statement as an analogy.
The key concept is delegation and resumption of flow.

Delegation and suspension: The main agent delegates a specific task to a sub-agent and temporarily suspends its own operation.
Task processing and result return: The sub-agent performs the delegated task and yields the result.
Resumption: The main agent resumes its next task after the sub-agent has completed processing.
In summary, this model efficiently structures the workflow by delegating specific tasks to sub-agents for processing.
"""
import time
def count_up_to(max_number):
    number = 0
    while number < max_number:
        # Returns the number and suspends function execution; resumes after processing is done.
        yield number  
        print("After yield in count_up_to:", number)
        number += 1

for num in count_up_to(5):
    print(num)  # Prints 0, 1, 2, 3, 4
    time.sleep(1)  # Waits 1 second
    print("Yielded in loop:", num)  # Yielded in loop: 0, 1, ...