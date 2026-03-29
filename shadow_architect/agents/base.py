from abc import ABC, abstractmethod
from typing import Dict, Any
import logging
from langchain_ollama import ChatOllama
from ..core.state import ArchitectState

# Configure professional logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class BaseAgent(ABC):
    """
    Abstract Base Class for all Shadow Architect Agents.
    Provides standardized LLM initialization, logging, and lifecycle management.
    """
    
    def __init__(self, model_name: str = "llama3"):
        """
        Initializes the agent with a specific LLM model.
        
        Args:
            model_name (str): The name of the Ollama model to use. Defaults to 'llama3'.
        """
        self.llm = ChatOllama(model=model_name, temperature=0)
        self.model_name = model_name
        self.logger = logging.getLogger(self.__class__.__name__)

    def _log(self, message: str, level: str = "info"):
        """
        Emits a standardized log message for the agent.
        
        Args:
            message (str): The message to log.
            level (str): The logging level ('info', 'warning', 'error', 'debug').
        """
        log_func = getattr(self.logger, level.lower(), self.logger.info)
        log_func(message)

    @abstractmethod
    async def call(self, state: ArchitectState) -> Dict[str, Any]:
        """
        The main entry point for the agent's logic within the LangGraph workflow.
        
        Args:
            state (ArchitectState): The current state of the architecture design process.
            
        Returns:
            Dict[str, Any]: A dictionary of state updates to be merged into the global state.
        """
        pass
