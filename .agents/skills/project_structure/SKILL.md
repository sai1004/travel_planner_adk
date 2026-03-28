Structure must separate **agents, tools, memory, orchestration, and configs**. Keep each agent isolated.

---

## 1. Root Structure

```
travel-planner/
│
├── app/                     # entry layer
├── agents/                  # all agents
├── tools/                   # external integrations
├── memory/                  # storage + retrieval
├── workflows/               # orchestration logic
├── schemas/                 # data contracts
├── configs/                 # settings
├── utils/                   # shared helpers
├── tests/                   # testing
├── requirements.txt
└── README.md
```

---

## 2. Agents Layer

Each agent = self-contained module

```
agents/
│
├── orchestrator/
│   ├── agent.py
│   ├── prompt.py
│   └── schema.py
│
├── planner/
│   ├── agent.py
│   ├── prompt.py
│   └── schema.py
│
├── research/
│   ├── agent.py
│   ├── prompt.py
│   └── schema.py
│
├── itinerary/
│   ├── agent.py
│   ├── prompt.py
│   └── schema.py
│
├── budget/
│   ├── agent.py
│   ├── prompt.py
│   └── schema.py
│
└── validator/
    ├── agent.py
    ├── prompt.py
    └── schema.py
```

**Rules**

- `agent.py` → ADK Agent definition
- `prompt.py` → system prompts
- `schema.py` → input/output contracts

---

## 3. Tools Layer

Wrap all APIs cleanly

```
tools/
│
├── flights/
│   ├── tool.py
│   └── client.py
│
├── hotels/
│   ├── tool.py
│   └── client.py
│
├── maps/
│   ├── tool.py
│   └── client.py
│
├── weather/
│   ├── tool.py
│   └── client.py
│
└── currency/
    └── tool.py
```

**Pattern**

- `tool.py` → ADK Tool definition
- `client.py` → raw API logic

---

## 4. Memory Layer

```
memory/
│
├── short_term/
│   └── session_store.py
│
├── long_term/
│   ├── vector_store.py
│   └── user_profile.py
│
└── memory_manager.py
```

---

## 5. Workflows (Orchestration)

Controls execution flow

```
workflows/
│
├── travel_workflow.py     # main pipeline
├── planner_flow.py
├── booking_flow.py
└── validation_flow.py
```

---

## 6. Schemas (Shared Contracts)

```
schemas/
│
├── itinerary_schema.py
├── budget_schema.py
├── travel_request.py
└── travel_response.py
```

Use strict structured outputs

---

## 7. App Layer (Entry Point)

```
app/
│
├── main.py              # API / CLI entry
├── routes.py            # if using FastAPI
└── controller.py        # calls orchestrator
```

---

## 8. Configs

```
configs/
│
├── settings.py          # env config
├── model_config.py      # LLM configs
└── tool_config.py       # API keys
```

---

## 9. Utils

```
utils/
│
├── logger.py
├── helpers.py
└── retry.py
```

---

## 10. Minimal ADK Wiring Example

```
app/main.py
```

```python
from agents.orchestrator.agent import orchestrator_agent
from workflows.travel_workflow import run_travel_flow

def main(user_input):
    return run_travel_flow(user_input)
```

---

```
workflows/travel_workflow.py
```

```python
from agents.planner.agent import planner_agent
from agents.research.agent import research_agent
from agents.itinerary.agent import itinerary_agent
from agents.budget.agent import budget_agent

def run_travel_flow(input):
    plan = planner_agent.run(input)
    data = research_agent.run(plan)
    itinerary = itinerary_agent.run(data)
    budget = budget_agent.run(itinerary)

    return {
        "itinerary": itinerary,
        "budget": budget
    }
```

---

## 11. Scaling Rule

- New feature → new agent (not modify existing)
- New API → new tool module
- Never mix orchestration inside agents

---

## 12. Clean Separation Principle

- Agents think
- Tools fetch
- Workflows control
- Memory remembers

No overlap.
