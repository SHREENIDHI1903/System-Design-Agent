import asyncio
from typing import Dict, Any, List
from .base import BaseAgent
from ..core.state import ArchitectState
from ..utils.mcp_client import MCPClient

class ScoutAgent(BaseAgent):
    """
    The Quality Assurance agent of the Shadow Architect.
    Uses the Model Context Protocol (MCP) to verify the proposed tech stack
    against real-world metadata (e.g., PyPI existence and health metrics).
    """

    def __init__(self, model_name: str = "llama3", mcp_mode: str = "mock"):
        """
        Initializes the ScoutAgent with an MCPClient.
        """
        super().__init__(model_name)
        self.mcp_client = MCPClient(mode=mcp_mode)

    async def call(self, state: ArchitectState) -> Dict[str, Any]:
        """
        Validates the proposed stack using real-time MCP verification.
        
        Args:
            state (ArchitectState): The current state of the architecture design process.
            
        Returns:
            Dict[str, Any]: Validation results and transition logic.
        """
        self._log("Starting real-time verification of the proposed stack...")
        stack = state.get("proposed_stack", {})
        
        if "error" in stack:
            self._log(f"Skipping verification: Stack contains errors: {stack.get('error')}", level="warning")
            return {
                "is_valid": False, 
                "validation_logs": state.get("validation_logs", []) + [f"Architect Error: {stack.get('error')}"],
                "current_agent": "Architect"
            }

        is_valid = True
        verification_logs = []
        
        # Identify components to verify
        components_to_check = {
            "Frontend": stack.get("frontend"),
            "Backend": stack.get("backend"),
            "Database": stack.get("database")
        }

        # Add additional libraries if present
        for lib in stack.get("libraries", []):
            components_to_check[f"Library ({lib})"] = lib

        # Perform MCP checks
        try:
            await self.mcp_client.connect()
            
            for component_name, package_name in components_to_check.items():
                if not package_name:
                    is_valid = False
                    msg = f"MISSING: {component_name} component is empty."
                    verification_logs.append(msg)
                    self._log(msg, level="warning")
                    continue

                self._log(f"Verifying {component_name}: '{package_name}'...")
                
                # Call the real-time MCP verification tool
                result = await self.mcp_client.verify_package(package_name)
                
                if not result["is_valid"]:
                    is_valid = False
                    reason = result["reason"]
                    msg = f"REJECTED [{component_name}]: {reason}"
                    verification_logs.append(msg)
                    self._log(msg, level="error")
                else:
                    msg = f"APPROVED [{component_name}]: {result['reason']}"
                    verification_logs.append(msg)
                    self._log(msg)

            await self.mcp_client.disconnect()
            
        except Exception as e:
            self._log(f"MCP Verification process failed: {str(e)}", level="error")
            is_valid = False # Fail secure
            verification_logs.append(f"System Error: MCP verification failed ({str(e)})")

        self._log(f"Verification complete. Stack Valid: {is_valid}")
        
        # Merging existing logs with new verification results
        final_logs = state.get("validation_logs", []) + verification_logs
        
        return {
            "is_valid": is_valid,
            "validation_logs": final_logs,
            "current_agent": "End" if is_valid else "Architect"
        }
