import asyncio
from shadow_architect.utils.mcp_client import MCPClient

async def test_mcp_client():
    print("--- Verifying MCPClient (Real-Time Mode) ---")
    client = MCPClient(mode="real")
    await client.connect()
    
    # Test valid package
    result_valid = await client.verify_package("fastapi")
    print(f"FastAPI result: {result_valid['is_valid']} - {result_valid['reason']}")
    
    # Test deprecated package
    result_deprecated = await client.verify_package("deprecated-lib")
    print(f"Deprecated result: {result_deprecated['is_valid']} - {result_deprecated['reason']}")
    
    # Test unpopular package
    result_unpopular = await client.verify_package("unpopular-db")
    print(f"Unpopular result: {result_unpopular['is_valid']} - {result_unpopular['reason']}")
    
    await client.disconnect()
    print("\n--- MCP Client Logic Verified ---")

if __name__ == "__main__":
    asyncio.run(test_mcp_client())
