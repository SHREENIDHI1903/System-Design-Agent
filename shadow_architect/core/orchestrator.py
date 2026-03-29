import logging
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

from .state import ArchitectState
from .config import settings
from ..agents.interviewer import InterviewerAgent
from ..agents.researcher import ResearcherAgent
from ..agents.architect import ArchitectAgent
from ..agents.scout import ScoutAgent
from ..agents.writer import WriterAgent

# Professional-grade logging
logger = logging.getLogger("Orchestrator")

class ShadowArchitectGraph:
    """
    Orchestrator for the Shadow Architect multi-agent workflow.
    Manages the transitions between Interviewer, Researcher, Architect, and Scout agents.
    """

    def __init__(self, model_name: Optional[str] = None, mcp_mode: Optional[str] = None):
        """
        Initializes the workflow agents and the graph topology.
        """
        self.settings = settings
        self.model_name = model_name or self.settings.MODEL_NAME
        self.mcp_mode = mcp_mode or self.settings.MCP_MODE
        
        # Initialize Agents
        self.interviewer = InterviewerAgent(self.model_name)
        self.researcher = ResearcherAgent(self.model_name)
        self.architect = ArchitectAgent(self.model_name)
        self.scout = ScoutAgent(self.model_name, self.mcp_mode)
        self.writer = WriterAgent(self.model_name)

    def build_graph(self, checkpointer: Optional[AsyncSqliteSaver] = None):
        """
        Defines the nodes and edges for the LangGraph workflow.
        """
        workflow = StateGraph(ArchitectState)

        # 1. Define Nodes (using call_with_retry for industrial resilience)
        workflow.add_node("Interviewer", self.interviewer.call_with_retry)
        workflow.add_node("Researcher", self.researcher.call_with_retry)
        workflow.add_node("Architect", self.architect.call_with_retry)
        workflow.add_node("Scout", self.scout.call_with_retry)
        workflow.add_node("Writer", self.writer.call_with_retry)

        # 2. Define Edges (The Core Loop)
        workflow.add_edge(START, "Interviewer")
        
        # Transition from Interviewer: 
        # If requirements are gathered -> Researcher -> Architect
        # If not -> END (user feedback)
        workflow.add_conditional_edges(
            "Interviewer",
            lambda x: "Researcher" if x.get("requirements") else END
        )
        
        # Researcher always moves to Architect
        workflow.add_edge("Researcher", "Architect")

        # After Architect proposes a stack, it MUST be verified by the Scout
        workflow.add_edge("Architect", "Scout")

        # The Scout decides if the project is finished or needs rework
        # If valid -> Writer -> END
        # If not -> Architect
        workflow.add_conditional_edges(
            "Scout",
            lambda x: "Writer" if x.get("is_valid") else "Architect"
        )
        
        # Writer is the final step
        workflow.add_edge("Writer", END)

        return workflow.compile(checkpointer=checkpointer)
