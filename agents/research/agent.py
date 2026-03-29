from google.adk.agents import Agent
from .prompt import RESEARCH_PROMPT
from tools.weather.tool import get_weather
from tools.flights.tool import search_flights
from tools.hotels.tool import search_hotels

research_agent = Agent(
    name="research_agent",
    model="gemini-flash-latest",
    description="Uses tools to research flights, hotels, and weather.",
    instruction=RESEARCH_PROMPT,
    tools=[get_weather, search_flights, search_hotels],
)
