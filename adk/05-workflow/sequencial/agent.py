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

from dotenv import load_dotenv
from google.adk.agents import SequentialAgent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

# `root_agent` defines a simple pipeline where each sub-agent runs in order.
# Use SequentialAgent when later steps depend on outputs produced by earlier steps.
# In this pipeline:
#  - `positive_critic` runs first to provide a positive critique,
#  - `negative_critic` runs next to provide a negative critique,
#  - `review_critic` runs last to review combined outputs and produce a final evaluation.
root_agent = SequentialAgent(
    name="pipeline_agent",
    sub_agents=[positive_critic, negative_critic, review_critic],
    description="This is an agent that sequentially executes agents(positive_critic, negative_critic, review_critic)",
)
