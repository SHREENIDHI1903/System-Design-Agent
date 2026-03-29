from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from langchain_ollama import ChatOllama
from ..core.state import ArchitectState
from ..core.config import settings

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
    
    def __init__(self, model_name: Optional[str] = None):
        """
        Initializes the agent with a specific LLM model.
        
        Args:
            model_name (str, optional): Override the default model from settings.
        """
        self.settings = settings
        model = model_name or self.settings.MODEL_NAME
        
        self.llm = ChatOllama(
            model=model, 
            temperature=self.settings.TEMPERATURE
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    async def call_with_retry(self, state: ArchitectState) -> Dict[str, Any]:
        """
        A resilient wrapper around the agent's core logic.
        """
        try:
            return await self.call(state)
        except Exception as e:
            self._log(f"Transient error in agent execution: {str(e)}", level="error")
            raise

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
