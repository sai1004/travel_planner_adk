# Travel Planner AI

A sophisticated AI-driven travel planning system built with the ADK (Agent Development Kit) framework. This project uses a multi-agent orchestration pattern to help users research, plan, and budget their perfect trips.

## Project Structure

```text
travel-planner/
├── .env              # Environment Configuration (API keys, etc.)
├── README.md         # Project Documentation
├── requirements.txt  # Project Dependencies
├── agents/           # Core Agents Layer
│   └── agent.py      # Main Root Agent Entry Point
├── tools/            # External integrations (Flights, Hotels, Weather, etc.)
├── workflows/        # Orchestration logic for multi-step tasks
├── memory/           # Storage and retrieval system
├── schemas/          # Data contracts and Pydantic models
├── configs/          # Settings and LLM configurations
├── utils/            # Shared helper functions
└── tests/            # Automated testing suite
```

## Technical Setup Guide

### 1. Prerequisites
- **Python 3.10+**: Ensure you have a modern Python version installed.
- **ADK installed**: The Agent Development Kit should be installed in your environment.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone <repository-url>
cd travel_planner
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory (or use the existing one) with your credentials:
```env
GOOGLE_API_KEY=your_google_api_key
# Additional keys if using other models/services
OPENAI_API_KEY=your_openai_api_key
```

## Running the Application

The application is fully compatible with the ADK CLI and Web UI.

### Option 1: ADK Web UI (Recommended)
This launches a FastAPI-based web server with a sophisticated developer interface.
```bash
# From the project root
PYTHONPATH=. adk web agents/ --port 8000
```
Then navigate to `http://127.0.0.1:8000` in your browser.

### Option 2: ADK Interactive CLI
For a terminal-based interactive session with the orchestrator:
```bash
# From the project root
PYTHONPATH=. adk run agents/agent.py
```

### Option 3: Manual Script Execution
You can also run the entry point directly:
```bash
python3 agents/agent.py
```

## Design Architecture

The Travel Planner employs the **Orchestrator-Worker** pattern. The `orchestrator_agent` serves as the central brain, delegating tasks to a team of specialized sub-agents:

| Agent | Responsibility |
| :--- | :--- |
| **Orchestrator** | Coordinates user requests and manages sub-agent flow. |
| **Planner** | Creates a high-level structure for the trip timeline. |
| **Research** | Fetches real-time data on destinations and attractions. |
| **Itinerary** | Generates detailed day-by-day plans. |
| **Budget** | Calculates estimates and manages cost constraints. |

## Development and Testing
Run tests using pytest:
```bash
pytest tests/
```
