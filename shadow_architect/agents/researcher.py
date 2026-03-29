import logging
from typing import Dict, Any, List
from duckduckgo_search import DDGS
from .base import BaseAgent
from ..core.state import ArchitectState

# Professional logging
logger = logging.getLogger("ResearcherAgent")

class ResearcherAgent(BaseAgent):
    """
    The Research agent of the Shadow Architect.
    Browses the web using DuckDuckGo to discover modern technical stacks
    and libraries that fit the user's requirements.
    """
    
    def __init__(self, model_name: str = "llama3"):
        """
        Initializes the ResearcherAgent.
        """
        super().__init__(model_name)

    async def call(self, state: ArchitectState) -> Dict[str, Any]:
        """
        Performs web research to find the best/modern libraries for the requirements.
        
        Args:
            state (ArchitectState): The current state of the architecture design process.
            
        Returns:
            Dict[str, Any]: Research notes and transition logic.
        """
        self._log("Starting real-time web research for modern tech components...")
        requirements = state.get("requirements", [])
        research_notes = []
        
        if not requirements:
            self._log("No requirements found to research.", level="warning")
            return {"research_notes": ["No requirements provided."], "current_agent": "Architect"}

        # Truncate requirements for shorter, more effective queries
        short_reqs = " ".join(requirements[:2])
        search_queries = [
            f"best modern backend framework for {short_reqs} 2024 2025",
            f"modern frontend stack for {short_reqs} 2024 2025",
            f"best database for {short_reqs} scalability 2025"
        ]

        try:
            with DDGS() as ddgs:
                for query in search_queries:
                    self._log(f"Searching: '{query}'...")
                    results = list(ddgs.text(query, max_results=3))
                    
                    if results:
                        # Extract snippets to form research notes
                        snippets = [f"- {r['title']}: {r['body']}" for r in results]
                        research_notes.append(f"### Research results for: {query}\n" + "\n".join(snippets))
                        self._log(f"Found {len(results)} relevant snippets.")
                    else:
                        self._log(f"No results found for: {query}", level="warning")

        except Exception as e:
            self._log(f"Web research failed: {str(e)}", level="error")
            research_notes.append(f"Error during research: {str(e)}")

        self._log(f"Research phase complete. Gathered {len(research_notes)} context blocks.")
        
        return {
            "research_notes": research_notes,
            "current_agent": "Architect"
        }
