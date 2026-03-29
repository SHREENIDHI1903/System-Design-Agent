from typing import List, Dict, Any, TypedDict, Optional

class ArchitectState(TypedDict):
    """The central state for the Shadow Architect workflow."""
    user_goal: str
    requirements: List[str]
    proposed_stack: Dict[str, Any]
    validation_logs: List[str]
    is_valid: bool
    current_agent: str
    research_notes: List[str]
    metadata: Optional[Dict[str, Any]]
