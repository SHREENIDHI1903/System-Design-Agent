import asyncio
import logging
from shadow_architect.core.orchestrator import ShadowArchitectGraph

# Configuring global industrial logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("shadow_architect.log")
    ]
)
logger = logging.getLogger("Main")

async def run_shadow_architect():
    """
    Entry point for the Shadow Architect Sprint 3 workflow.
    """
    logger.info("Initializing Shadow Architect - Sprint 3: The Hands (MCP & Research Integration)")
    
    # Initialize the orchestrator (real-time mode enabled)
    orchestrator = ShadowArchitectGraph(model_name="llama3", mcp_mode="real")
    app = orchestrator.build_graph()

    # Initial state with the new research_notes field
    initial_state = {
        "user_goal": "I want to build a highly scalable real-time chat application with group messaging.",
        "requirements": [],
        "research_notes": [],
        "proposed_stack": {},
        "validation_logs": [],
        "is_valid": False,
        "current_agent": "Interviewer",
        "metadata": {}
    }

    logger.info("Starting the multi-agent workflow...")
    
    # Execute the graph
    async for event in app.astream(initial_state):
        for node_name, node_state in event.items():
            logger.info(f"--- Finished Node: {node_name} ---")
            # The last state in the stream provides the current progress
            # print(node_state) 

    logger.info("Workflow execution final status reached.")

if __name__ == "__main__":
    try:
        asyncio.run(run_shadow_architect())
    except KeyboardInterrupt:
        logger.info("Shadow Architect terminated by user.")
    except Exception as e:
        logger.error(f"Critical error in main entry point: {str(e)}")
