from google.adk.agents import Agent
from .prompt import ITINERARY_PROMPT

itinerary_agent = Agent(
    name="itinerary_agent",
    model="gemini-flash-latest",
    description="Creates a day-by-day itinerary based on research data.",
    instruction=ITINERARY_PROMPT,
)
