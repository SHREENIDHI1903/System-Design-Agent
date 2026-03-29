import httpx
from fastmcp import FastMCP
import logging

# Set up logging to stderr (crucial for stdio MCP servers)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PyPIServer")

mcp = FastMCP("ShadowPyPI")

@mcp.tool()
async def get_package_info(name: str) -> str:
    """
    Fetches real-time metadata from PyPI for a given package name.
    
    Args:
        name (str): The name of the package to look up (e.g., 'fastapi').
        
    Returns:
        str: A JSON string containing version, summary, and project links.
    """
    url = f"https://pypi.org/pypi/{name}/json"
    logger.info(f"Fetching metadata for package: {name}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 404:
                return f"Error: Package '{name}' not found on PyPI."
            
            response.raise_for_status()
            data = response.json()
            
            info = data.get("info", {})
            metadata = {
                "name": info.get("name"),
                "version": info.get("version"),
                "summary": info.get("summary"),
                "home_page": info.get("home_page"),
                "project_urls": info.get("project_urls"),
                "author": info.get("author"),
                "license": info.get("license"),
            }
            
            import json
            return json.dumps(metadata, indent=2)
            
        except httpx.HTTPStatusError as e:
            return f"HTTP Error: {e.response.status_code} while fetching {name}"
        except Exception as e:
            return f"System Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
