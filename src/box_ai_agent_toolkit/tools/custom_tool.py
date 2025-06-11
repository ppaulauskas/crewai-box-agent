from crewai.tools import BaseTool
from typing import Type
from typing import List
from pydantic import BaseModel, Field
from box_ai_agents_toolkit import get_ccg_client, box_search, box_file_ai_ask

class BoxSearchInput(BaseModel):
    """Input schema BoxSearch"""
    query: str = Field(..., description="The search query to use for Box search.")

class BoxSearch(BaseTool):
    name: str = "Search for files in Box"
    description: str = (
        "This tool is useful for searching for files in Box based on the user's query."
    )
    args_schema: Type[BaseModel] = BoxSearchInput

    def _run(self, query: str) -> str:
            client = get_ccg_client()
            search_results = box_search(client, query)

            return search_results
    
class BoxAIFileInput(BaseModel):
    """Input schema for BoxAIFileAsk."""
    file_id: str = Field(..., description="The file ID in Box to ask a Box AI a question about.")
    prompt: str = Field(..., description="The question to ask Box AI.")

class BoxAIFile(BaseTool):
    name: str = "Ask Box AI about a file"
    description: str = (
        "This tool is useful for asking Box AI a question about a specific file in Box."
    )
    args_schema: Type[BaseModel] = BoxAIFileInput

    def _run(self, file_id: str, prompt: str) -> str:
            client = get_ccg_client()
            response = box_file_ai_ask(client, file_id, prompt)

            return response