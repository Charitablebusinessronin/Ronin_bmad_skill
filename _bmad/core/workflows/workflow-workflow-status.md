---
name: 'workflow-status'
slug: 'workflow-status'
type: 'workflow'
---

# Notion AI System Instructions: Workflow Status

## Workflow Identity

**Name:** workflow-status
**Title:** Workflow Status Check and Master Router
**Module:** BMM (Business Method Module)
**Workflow Type:** BMAD

## Purpose

Lightweight status checker that answers “what should I do now?” for any agent. Reads workflow status tracking to provide recommendations.

## Description

Master workflow router and status tracker. This workflow checks the current state of a project and provides recommendations on what should be done next. It’s the starting point for any BMAD agent to understand project status and determine next steps.

## How to Execute This Workflow in Notion

### Activation

When you need to check project status or determine next steps:

1. **Read workflow status** from Notion database or pages
1. **Analyze current project state** based on documentation
1. **Provide recommendations** for next steps
1. **Guide user** to appropriate next workflow

### Execution Steps in Notion

1. **Status Review**
1. **Recommendation Generation**
1. **Guidance**

### Natural Language Commands

- “Check workflow status” or “What’s the status?”
- “What should I do next?” or “Next steps”
- “Review workflow” or “Check project status”

### Workflow Outputs

- Status summary of current project state
- Recommendation for next workflow
- Context and guidance for next steps

### Related Agents

- All BMAD agents use this workflow
- Gilliam (BMAD Master orchestration)
- Product Manager (planning guidance)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Status Check

🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: 'workflow status project progress blockers [PROJECT_NAME]',
  group_id: '[current-project]', // e.g., "diff-driven-saas"
})
```

**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Recent Events: [list titles]
- Blockers/Issues: [list if any]
- Last Completed Phase: [phase name]
```

**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this project.
Proceeding without workflow history.
Risk: May miss important context from previous sessions.
```

❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Status Check

**When to Log:**

- After completing status assessment
- When routing to next workflow
- When blocker is identified
- When project phase changes
  **1. Create Event:**

```javascript
create_entities({
  entities: [
    {
      name: 'Status Check - [project_name]',
      entityType: 'Event',
      observations: [
        'project: [name]',
        'current_phase: [phase]',
        'recommended_workflow: [workflow]',
        'blockers: [list or none]',
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
      name: 'Outcome - Status - [project_name]',
      entityType: 'Outcome',
      observations: [
        'status: [On Track/Blocked/Needs Attention]',
        'next_action: [recommended workflow]',
        'progress_percentage: [estimate]',
        'critical_path: [items]',
      ],
    },
  ],
})
```

**3. Link Event → Outcome:**

```javascript
create_relations({
  relations: [{ from: '[Event name]', to: '[Outcome name]', relationType: 'RESULTED_IN' }],
})
```

### Exit Validation (Required before routing)

**Validation Checklist:**

---

## Integration Details

**Module:** BMM
**Phase Focus:** All Phases (Master Router)
**Related Workflows:**

- All BMAD workflows (routes to them)
  **Integration Points:** Notion, Neo4j MCP
  **Platform:** Claude (via Notion AI)
