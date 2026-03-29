from agents.orchestrator.agent import orchestrator_agent

async def run_travel_planner_flow(user_query: str):
    """Executes the travel planning workflow using the orchestrator agent.
    
    This function leverages the ADK agent hierarchy to process a user request.
    The orchestrator manages the Planner, Research, Itinerary, and Budget agents.
    """
    response = await orchestrator_agent.run(user_query)
    return response
