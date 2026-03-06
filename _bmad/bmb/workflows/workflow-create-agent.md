---
name: 'create-agent'
slug: 'create-agent'
type: 'workflow'
---

# Notion AI System Instructions: Create Agent

## Workflow Identity

**Name:** create-agent
**Title:** Create Agent
**Module:** BMB (BMad Method Builder)
**Workflow Type:** BMAD

## Purpose

Interactive workflow to build BMAD Core compliant agents (YAML source compiled to .md during install) with optional brainstorming, persona development, and command structure.

## Description

Interactive workflow builder for creating new BMAD agents. Guides through the process of building BMAD Core compliant agents with proper structure, persona development, communication styles, and menu/command patterns. Includes optional brainstorming phase for agent design.

## How to Execute This Workflow in Notion

### Activation

When you need to create a new BMAD agent:

1. **Guide through agent creation** conversationally
1. **Develop agent persona** and characteristics
1. **Define workflows** and capabilities
1. **Create agent documentation** in Notion

### Execution Steps in Notion

1. **Agent Design**
1. **Structure Creation**
1. **Documentation**

### Natural Language Commands

- “Create agent” or “Build new agent”
- “Design agent” or “Agent builder”
- “New BMAD agent” or “Agent creation”

### Workflow Inputs

- Agent concept or requirements
- Example agents (reference)
- Agent architecture patterns (reference)

### Workflow Outputs

- Agent system instructions in Notion
- Agent documentation
- Integration configuration

### Related Agents

- BMad Builder (primary)
- Gilliam (BMAD Master orchestration)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Workflow Start

🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: 'agent creation BMAD persona design [AGENT_NAME]',
  group_id: '[current-project]', // e.g., "diff-driven-saas"
})
```

**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Relevant Insights: [list titles]
- Past Agent Patterns: [list if any]
- Known Issues: [list if any]
```

**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this agent creation.
Proceeding without insights from past sessions.
Risk: May repeat previous agent design mistakes.
```

❌ DO NOT proceed until memory retrieval completes
❌ DO NOT skip this step even if user says "just start"
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Workflow Completion

**When to Log:**

- After creating new agent successfully
- After agent persona validation completes
- When agent pattern is reusable
- When agent design decision is made
  **1. Create Event:**

```javascript
create_entities({
  entities: [
    {
      name: 'Agent Created - [agent_name]',
      entityType: 'Event',
      observations: [
        'agent_name: [name]',
        'agent_role: [role]',
        'module: [BMB/BMM/CIS/CORE]',
        'inspired_by: [legendary figure]',
        'timestamp: [ISO 8601]',
      ],
    },
  ],
})
```

**2. Create Outcome:**

```javascript
create_entities({
  entities: [
    {
      name: 'Outcome - [Success/Fail] - [agent_name]',
      entityType: 'Outcome',
      observations: [
        'status: [Success/Fail]',
        'persona_validated: [true/false]',
        'workflows_assigned: [list]',
        'integration_verified: [true/false]',
      ],
    },
  ],
})
```

**3. Create Insight (if pattern learned):**

```javascript
create_entities({
  entities: [
    {
      name: 'Insight - Agent Pattern - [pattern_name]',
      entityType: 'Insight',
      observations: [
        'pattern: [description]',
        'applicability: [when to use]',
        'benefits: [why it works]',
      ],
    },
  ],
})
```

**4. Link Event → Outcome → Insight:**

```javascript
create_relations({
  relations: [
    { from: '[Event name]', to: '[Outcome name]', relationType: 'RESULTED_IN' },
    { from: '[Outcome name]', to: '[Insight name]', relationType: 'INFORMED' },
  ],
})
```

### Exit Validation (Required before workflow completion)

**Query Neo4j for Events logged:**

```javascript
search_memories({
  query: 'agent creation [agent_name] today',
  group_id: '[current-project]',
})
```

**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before completing workflow

---

## Integration Details

**Module:** BMB
**Phase Focus:** Builder
**Related Workflows:**

- create-workflow (for agent workflows)
- create-module (for module agents)
  **Integration Points:** Notion, Neo4j MCP
  **Platform:** Claude (via Notion AI)
