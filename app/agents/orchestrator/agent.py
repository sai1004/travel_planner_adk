from google.adk.agents import Agent
from .prompt import ORCHESTRATOR_PROMPT
from agents.planner.agent import planner_agent
from agents.research.agent import research_agent
from agents.itinerary.agent import itinerary_agent
from agents.budget.agent import budget_agent

orchestrator_agent = Agent(
    name="orchestrator_agent",
    model="gemini-flash-latest",
    description="The central brain of the Travel Planner system.",
    instruction=ORCHESTRATOR_PROMPT,
    sub_agents=[planner_agent, research_agent, itinerary_agent, budget_agent],
)
