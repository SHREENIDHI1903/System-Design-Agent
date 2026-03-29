import logging
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END

from .state import ArchitectState
from ..agents.interviewer import InterviewerAgent
from ..agents.researcher import ResearcherAgent
from ..agents.architect import ArchitectAgent
from ..agents.scout import ScoutAgent

# Professional-grade logging
logger = logging.getLogger("Orchestrator")

class ShadowArchitectGraph:
    """
    Orchestrator for the Shadow Architect multi-agent workflow.
    Manages the transitions between Interviewer, Researcher, Architect, and Scout agents.
    """

    def __init__(self, model_name: str = "llama3", mcp_mode: str = "mock"):
        """
        Initializes the workflow agents and the graph topology.
        """
        self.model_name = model_name
        self.mcp_mode = mcp_mode
        
        # Initialize Agents
        self.interviewer = InterviewerAgent(model_name)
        self.researcher = ResearcherAgent(model_name)
        self.architect = ArchitectAgent(model_name)
        self.scout = ScoutAgent(model_name, mcp_mode)

    def build_graph(self):
        """
        Defines the nodes and edges for the LangGraph workflow.
        """
        workflow = StateGraph(ArchitectState)

        # 1. Define Nodes
        workflow.add_node("Interviewer", self.interviewer.call)
        workflow.add_node("Researcher", self.researcher.call)
        workflow.add_node("Architect", self.architect.call)
        workflow.add_node("Scout", self.scout.call)

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
        workflow.add_conditional_edges(
            "Scout",
            lambda x: "Architect" if not x.get("is_valid") else END
        )

        return workflow.compile()
