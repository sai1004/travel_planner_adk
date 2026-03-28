from google.adk.agents import Agent
from .prompt import BUDGET_PROMPT

budget_agent = Agent(
    name="budget_agent",
    model="gemini-flash-latest",
    description="Provides budget analysis for the trip.",
    instruction=BUDGET_PROMPT,
)
