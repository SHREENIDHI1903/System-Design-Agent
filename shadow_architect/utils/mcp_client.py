import asyncio
import logging
import sys
import os
import json
from typing import Dict, Any, Optional, List
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Industrial Level Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MCPClient")

class MCPClient:
    """
    A professional-grade MCP Client wrapper supporting both a live
    PyPI metadata server and a mock mode for testing.
    """
    
    def __init__(self, mode: str = "mock", config: Optional[Dict[str, Any]] = None):
        """
        Initializes the client.
        
        Args:
            mode (str): 'mock' or 'real'.
            config (Dict): Configuration for the real server (command, args, env).
        """
        self.mode = mode
        self.config = config or {}
        self.session: Optional[ClientSession] = None
        self._client_context = None

    async def connect(self):
        """Establishes connection to the MCP server if in 'real' mode."""
        if self.mode == "mock":
            logger.info("Operating in MOCK mode. No real connection established.")
            return

        # Default path to the pypi_server.py if not provided
        server_script = self.config.get("script", os.path.join(
            os.path.dirname(__file__), "pypi_server.py"
        ))

        server_params = StdioServerParameters(
            command=sys.executable,
            args=[server_script],
            env=os.environ.copy()
        )
        
        logger.info(f"Connecting to real-time MCP server via stdio: {server_script}")
        
        try:
            self._client_context = stdio_client(server_params)
            read, write = await self._client_context.__aenter__()
            self.session = ClientSession(read, write)
            await self.session.__aenter__()
            await self.session.initialize()
            logger.info("Real-time MCP connection established.")
        except Exception as e:
            logger.error(f"Failed to connect to real-time MCP server: {str(e)}")
            raise

    async def disconnect(self):
        """Gracefully shuts down the MCP session."""
        if self.mode == "mock" or not self.session:
            return
        
        try:
            await self.session.__aexit__(None, None, None)
            await self._client_context.__aexit__(None, None, None)
            logger.info("MCP Client disconnected.")
        except Exception as e:
            logger.error(f"Error during MCP disconnection: {str(e)}")

    async def fetch_package_metadata(self, package_name: str) -> Dict[str, Any]:
        """
        Fetches metadata for a given package.
        Uses the real 'get_package_info' tool if in real mode.
        """
        if self.mode == "mock":
            return await self._mock_fetch_metadata(package_name)
        
        if not self.session:
            raise ConnectionError("MCP Client is not connected. Call connect() first.")

        try:
            # The tool name defined in pypi_server.py
            result = await self.session.call_tool("get_package_info", {"name": package_name})
            
            # FastMCP tools return content[0].text for string outputs
            if result.content and len(result.content) > 0:
                text_content = result.content[0].text
                
                # Check if it looks like JSON
                if text_content.startswith("{"):
                    return json.loads(text_content)
                
                # If it's an error message or string
                if "Error" in text_content:
                    return {"error": text_content}
                
                return {"summary": text_content}
            
            return {"error": "No content returned from MCP tool."}
            
        except Exception as e:
            logger.error(f"Failed to fetch metadata for {package_name}: {str(e)}")
            return {"error": f"MCP Tool Call Error: {str(e)}"}

    async def _mock_fetch_metadata(self, package_name: str) -> Dict[str, Any]:
        """Simulates MCP tool responses for development."""
        await asyncio.sleep(0.1)
        
        mock_registry = {
            "fastapi": {"name": "fastapi", "version": "0.110.0", "summary": "FastAPI framework..."},
            "react": {"name": "react", "version": "18.2.0", "summary": "React is a JS library..."},
            "postgresql": {"name": "psycopg2", "version": "2.9.9", "summary": "PostgreSQL adapter..."},
            "deprecated-lib": {"error": "Package 'deprecated-lib' is deprecated."},
        }
        
        return mock_registry.get(package_name.lower(), {"error": "Package not found in mock registry."})

    async def verify_package(self, package_name: str) -> Dict[str, Any]:
        """
        High-level verification logic focusing on existence and metadata quality.
        """
        metadata = await self.fetch_package_metadata(package_name)
        
        if "error" in metadata:
            return {"is_valid": False, "reason": metadata["error"]}
        
        # In real-time mode, we consider it valid if metadata exists
        return {
            "is_valid": True, 
            "reason": f"Real-time verification successful: Version {metadata.get('version', 'unknown')} found.",
            "metadata": metadata
        }
