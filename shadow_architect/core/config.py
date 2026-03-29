from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    """
    Centralized configuration for the Shadow Architect.
    Uses pydantic-settings to validate environment variables.
    """
    model_config = SettingsConfigDict(env_prefix="SHADOW_", env_file=".env", extra="ignore")

    # LLM Configuration
    MODEL_NAME: str = "llama3"
    TEMPERATURE: float = 0.0
    
    # RAG Configuration
    CHROMA_PATH: str = "chroma_db"
    KNOWLEDGE_BASE_PATH: str = "knowledge_base"
    
    # MCP Configuration
    MCP_MODE: str = "mock"  # Can be 'real' or 'mock'
    
    # Observability
    LANGSMITH_TRACING: bool = False
    LANGSMITH_API_KEY: Optional[str] = None
    LANGSMITH_PROJECT: str = "shadow-architect-agent"

# Global settings instance
settings = Settings()

def get_settings():
    """Returns the global settings instance."""
    return settings
