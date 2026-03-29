import os
from typing import Dict, Any
from .base import BaseAgent
from ..core.state import ArchitectState

class WriterAgent(BaseAgent):
    """
    Final node in the Shadow Architect workflow.
    Synthesizes the entire session into professional design artifacts.
    """

    async def call(self, state: ArchitectState) -> Dict[str, Any]:
        """
        Invokes the LLM to create a finalized System Design Document and Docker Compose.
        """
        self._log("Synthesizing final architectural artifacts via LLM...")
        
        # Prepare context for the LLM
        context = f"""
        User Goal: {state.get('user_goal')}
        Core Requirements: {", ".join(state.get('requirements', []))}
        Proposed Tech Stack: {state.get('proposed_stack')}
        Research Notes: {", ".join(state.get('research_notes', []))}
        Validation Logs: {", ".join(state.get('validation_logs', []))}
        """

        prompt = f"""
        You are a Senior System Architect. Based on the following context, generate two separate artifacts.
        
        CONTEXT:
        {context}

        ARTIFACT 1: System Design Document (Markdown)
        - Include an Executive Summary.
        - Detailed Technical Stack explanation.
        - A section on Architectural Patterns used (based on the research notes).
        - A comprehensive 'API Design' section documenting core endpoints (REST/gRPC/GraphQL).
        - Security and Scalability considerations.

        ARTIFACT 2: Docker Compose File (YAML)
        - Provide a production-ready docker-compose.yml using the proposed stack.
        - Ensure proper service dependencies and environment variables.

        Format your final response clearly, separating the two artifacts with a unique separator like '---DOCUMENT_SEPARATOR---'.
        """

        # Invoke the LLM for synthesis
        response = await self.llm.ainvoke(prompt)
        content = response.content

        # Split artifacts
        parts = content.split('---DOCUMENT_SEPARATOR---')
        system_design = parts[0].strip() if len(parts) > 0 else "Failed to generate design."
        docker_compose = parts[1].strip() if len(parts) > 1 else "version: '3.8'\nservices: {}"

        # 3. Persistence: Write to filesystem (Sprint 4 Requirement)
        try:
            with open("system_design.md", "w", encoding="utf-8") as f:
                f.write(system_design)
            
            with open("docker-compose.yml", "w", encoding="utf-8") as f:
                f.write(docker_compose)
                
            self._log("Successfully wrote artifacts to workspace: system_design.md, docker-compose.yml")
        except Exception as e:
            self._log(f"Failed to write artifacts to disk: {str(e)}", level="error")

        return {
            "metadata": {
                "system_design_path": "system_design.md",
                "docker_compose_path": "docker-compose.yml"
            },
            "current_agent": "Writer"
        }
