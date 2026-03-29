from google.adk.agents import Agent
from .prompt import PLANNER_PROMPT

planner_agent = Agent(
    name="planner_agent",
    model="gemini-flash-latest",
    description="Breaks down a travel request into a structured plan.",
    instruction=PLANNER_PROMPT,
)
