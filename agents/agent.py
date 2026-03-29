import os
import sys

# Add the project root directory to sys.path to resolve module imports correctly
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from agents.orchestrator.agent import orchestrator_agent

# The entry point for the ADK web server and CLI.
# The 'adk web' and 'adk run' commands will look for this root_agent.
root_agent = orchestrator_agent
