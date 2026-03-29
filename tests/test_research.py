import asyncio
import logging
from shadow_architect.agents.researcher import ResearcherAgent

# Set up logging to see the research process
logging.basicConfig(level=logging.INFO)

async def test_researcher():
    print("--- Verifying ResearcherAgent (DuckDuckGo Search) ---")
    researcher = ResearcherAgent(model_name="llama3")
    
    # Mock state with requirements
    mock_state = {
        "requirements": ["FastAPI", "PostgreSQL"],
        "research_notes": []
    }
    
    try:
        result = await researcher.call(mock_state)
        print("\n--- Research Results ---")
        for note in result["research_notes"]:
            print(note[:200] + "...") # Print first 200 chars of each result
            
        print("\n--- Next Agent: " + result["current_agent"] + " ---")
        
    except Exception as e:
        print(f"Research Test Failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_researcher())
