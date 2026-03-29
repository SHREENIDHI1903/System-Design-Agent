import re
import json
import logging
from typing import Dict, Any, List, Optional
from langchain_ollama import OllamaLLM
from .base import BaseAgent
from ..core.state import ArchitectState

# Professional-grade logging
logger = logging.getLogger("ArchitectAgent")

class ArchitectAgent(BaseAgent):
    """
    The System Designer of the Shadow Architect.
    Uses requirements AND research notes to propose a modern technical stack.
    """

    def __init__(self, model_name: str = "llama3"):
        """
        Initializes the ArchitectAgent with a specific reasoning model.
        """
        super().__init__(model_name)

    async def call(self, state: ArchitectState) -> Dict[str, Any]:
        """
        Proposes a modern tech stack based on requirements and research results.
        
        Args:
            state (ArchitectState): The current state of the architecture design process.
            
        Returns:
            Dict[str, Any]: A proposed stack and architectural thinking.
        """
        self._log("Synthesizing requirements with real-time research notes...")
        
        requirements = ", ".join(state.get("requirements", []))
        research_context = "\n".join(state.get("research_notes", ["No research available."]))
        
        prompt = f"""
        You are a Senior System Architect. Using the Requirements and the Research Notes provided below, 
        propose a modern, high-quality technical stack. 
        
        If the Research Notes contain newer or more popular libraries than traditional patterns, 
        prefer the research-backed choices.

        Requirements: {requirements}
        
        ---
        Real-Time Research Context:
        {research_context}
        ---

        Your output MUST be a valid JSON object with ONLY these fields:
        "frontend": (string)
        "backend": (string)
        "database": (string)
        "libraries": (list of strings)
        "reasoning": (string explaining why this stack was chosen over alternatives)

        JSON Output:
        """
        
        try:
            response = await self.llm.ainvoke(prompt)
            proposed_stack = self._parse_json_response(response)
            self._log(f"Proposed Stack: {proposed_stack.get('backend')} / {proposed_stack.get('frontend')}")
            
            return {
                "proposed_stack": proposed_stack,
                "current_agent": "Scout" # Hand over to the Scout for MCP verification
            }
            
        except Exception as e:
            self._log(f"Architecture proposal failed: {str(e)}", level="error")
            return {
                "proposed_stack": {"error": f"LLM Inference Error: {str(e)}"},
                "current_agent": "End"
            }

    def _parse_json_response(self, text: str) -> Dict[str, Any]:
        """
        Robustly extracts JSON from LLM string output using regex.
        """
        try:
            # Look for structured JSON block
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                return json.loads(match.group())
            return {"error": "No valid JSON found in LLM response."}
        except Exception as e:
            return {"error": f"JSON Parsing Error: {str(e)}"}
