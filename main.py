import asyncio
import logging
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
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
    Entry point for the Shadow Architect Sprint 4: Industrialization.
    Now supports persistence and resilient multi-agent execution.
    """
    logger.info("Initializing Shadow Architect - Sprint 4: Industrialization")
    
    # Initialize the orchestrator (real-time mode enabled if configured)
    orchestrator = ShadowArchitectGraph()
    
    # Initialize Persistence (Sprint 4 Feature - Async Mode)
    async with AsyncSqliteSaver.from_conn_string("checkpoints.db") as checkpointer:
        app = orchestrator.build_graph(checkpointer=checkpointer)

        # Thread configuration for session isolation
        config = {"configurable": {"thread_id": "session_1"}}

        # Initial state with the research_notes field
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

        logger.info("Starting the resilient multi-agent workflow...")
        
        # Execute the graph with persistence config
        async for event in app.astream(initial_state, config=config):
            for node_name, node_state in event.items():
                logger.info(f"--- Finished Node: {node_name} ---")
                if node_name == "Writer":
                    logger.info("Architectural artifacts generated in metadata.")

    logger.info("Workflow execution final status reached.")

if __name__ == "__main__":
    try:
        asyncio.run(run_shadow_architect())
    except KeyboardInterrupt:
        logger.info("Shadow Architect terminated by user.")
    except Exception as e:
        logger.error(f"Critical error in main entry point: {str(e)}")
