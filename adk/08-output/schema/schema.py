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

from pydantic import BaseModel, Field

class SearchResult(BaseModel):
    """
    Pydantic model representing the structure of a search result.

    Attributes:
        query (str): The user's query string.
        intention (str): The user's intention or purpose for asking the query.
        result (str): The results or answer corresponding to the query.
    """
    # ...existing code...
    query: str = Field(..., title="query", description="user's query")
    intention: str = Field(..., title="intention", description="user's intention to ask")
    result: str = Field(..., title="result", description="results")


""" JSON Format of schema. 

search_result = {
    "title": "search_results",
    "type": "OBJECT",
    "description": "search results",
    "required": ["query", "intention","result"],
    "properties": {
      "query": {
        "title": "query",
        "type": "STRING",
        "description": "user's query"
      },
      "intention": {
        "title": "intention",
        "type": "STRING",
        "description": "user's intention to ask"
	  },
      "result": {
        "title": "result",
        "type": "STRING",
        "description": "results"
      },	  
    },
    "property_ordering": ["query", "intention", "results"]
}    

"""