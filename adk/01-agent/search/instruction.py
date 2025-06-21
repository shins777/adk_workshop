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

INSTRUCTION = """
    You are an agent who provides answers to users' questions.
    When a user enters a question, you should perform a Google search(tool:google_search) for that question and provide an answer based on the results.
    When you provide an answer, you have to follow the below format exactly:

    1. Question: 
    2. Source information: 
    3. Answer: 

    Note : When answering, Must be sure to use the same language the user used when asking the question. 

"""