Core idea: break the system into specialized agents, each with a narrow role, coordinated by an orchestrator. Use tools + memory + planner loop.

---

## 1. System Architecture (High-Level)

**User → Orchestrator Agent → Specialized Agents → Tools/APIs → Response**

Agents do not talk randomly. All flow is controlled.

---

## 2. Agentic Design Pattern

### (A) Orchestrator Agent (Brain)

- Takes user query: “Plan 5-day trip to Bali under ₹50k”
- Breaks into tasks
- Decides which agent to call
- Merges outputs

Pattern:

- Intent detection
- Task decomposition
- Delegation
- Aggregation

---

### (B) Planner Agent

Creates structured plan before execution

Output example:

```
1. Get destination info
2. Fetch flights
3. Find hotels
4. Create itinerary
5. Estimate budget
```

Pattern:

- Tree-of-thought / step planning
- No API calls

---

### (C) Research Agent

Finds raw data

Tools:

- Flights API
- Hotel APIs
- Maps
- Weather

Responsibilities:

- Fetch options
- Normalize data

---

### (D) Itinerary Agent

Turns data → day-wise plan

Output:

```
Day 1: Arrival + Beach
Day 2: Temples + Local food
...
```

Pattern:

- Context-aware generation
- Uses preferences (budget, pace, interests)

---

### (E) Budget Agent

- Aggregates cost
- Optimizes choices

Logic:

- Flight + hotel + activities
- Suggest cheaper alternatives

---

### (F) Personalization Agent

- Uses memory (past trips, preferences)
- Adjusts plan

Example:

- Avoids nightlife if user never chooses it

---

### (G) Validator Agent

- Checks consistency
- Fixes issues

Checks:

- Time conflicts
- Budget overflow
- Travel feasibility

---

## 3. Core Agent Loop (Execution Pattern)

Use iterative loop:

```
while not done:
    think
    choose agent/tool
    execute
    observe
```

This is ReAct-style reasoning.

---

## 4. Tool Layer

Each agent uses tools, not raw internet.

Examples:

- Flight tool
- Hotel search tool
- Maps tool
- Currency converter

Design:

```
Tool = function + schema + API wrapper
```

---

## 5. Memory Design

### Short-Term Memory

- Current trip context
- Stored in session

### Long-Term Memory

- User preferences
- Past trips

Storage:

- Vector DB (semantic)
- Key-value (structured)

---

## 6. Data Flow Example

User: “3-day Goa trip under ₹20k”

1. Orchestrator → Planner
2. Planner → steps
3. Orchestrator calls:
   - Research Agent (hotels, transport)
   - Budget Agent

4. Itinerary Agent builds plan
5. Validator checks
6. Final response assembled

---

## 7. Google ADK Mapping

In Google ADK:

- Each agent = `Agent`
- Tools = `Tool`
- Orchestrator = Parent agent
- Communication = structured messages

Pattern in ADK:

```
RootAgent
 ├── PlannerAgent
 ├── ResearchAgent
 ├── BudgetAgent
 ├── ItineraryAgent
 └── ValidatorAgent
```

Use:

- function calling
- tool binding
- state passing

---

## 8. Control Patterns

### Sequential

Planner → Research → Itinerary → Budget

### Parallel

Flights + Hotels fetched at same time

### Hierarchical

Orchestrator → sub-agents

### Reflection Loop

Validator → sends back for correction

---

## 9. Minimal MVP Design

Start with:

- Orchestrator
- Research Agent
- Itinerary Agent
- Budget Agent

Skip:

- Personalization
- Validator (initially)

---

## 10. Failure Handling

- Tool failure → fallback options
- Missing data → ask user OR assume defaults
- Budget overflow → auto-adjust plan

---

## 11. Output Structure

Always return structured JSON:

```
{
  destination,
  itinerary: [],
  flights: [],
  hotels: [],
  total_cost,
  notes
}
```

---

## 12. Scaling Later

- Add real-time pricing
- Add booking integration
- Add user profiles
- Add multi-destination planning
- Add voice interface

---

This is the stable agentic pattern:

**Planner → Executor Agents → Validator → Aggregator (Orchestrator control loop)**
