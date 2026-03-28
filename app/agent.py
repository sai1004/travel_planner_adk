import sys
import os

# Add the local app directory to sys.path to resolve module imports correctly
sys.path.append(os.path.dirname(__file__))

from agents.orchestrator.agent import orchestrator_agent

# The entry point for the ADK web server and CLI.
# The 'adk web' and 'adk run' commands will look for this root_agent.
root_agent = orchestrator_agent
