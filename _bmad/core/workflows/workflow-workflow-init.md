---
name: 'workflow-init'
slug: 'workflow-init'
type: 'workflow'
---

# Notion AI System Instructions: Workflow Init

## Workflow Identity

**Name:** workflow-init
**Title:** Workflow Initialization
**Module:** BMM (Business Method Module)
**Workflow Type:** BMAD

## Purpose

Initialize a new BMM project by determining level, type, and creating workflow path.

## Description

Lightweight initialization workflow that sets up a new project by determining the project level (0-4), project type, and creating the initial workflow status tracking file. This is the entry point for new projects using the BMAD Method.

## How to Execute This Workflow in Notion

### Activation

When you need to start a new BMAD project or initialize workflow tracking:

1. **Guide the user** through project initialization questions
1. **Determine project level** (0-4) based on complexity
1. **Identify project type** (feature, bug fix, enhancement, etc.)
1. **Create Notion pages/databases** for workflow status tracking
1. **Set up project structure** in Notion

### Execution Steps in Notion

1. **Project Discovery**
1. **Workflow Path Selection**
1. **Initial Documentation**

### Natural Language Commands

- “Initialize workflow” or “Start new project”
- “Set up BMAD project” or “Create workflow status”
- “Begin new workflow” or “Initialize project”

### Workflow Outputs

- Project workflow status page in Notion
- Initial project documentation structure
- Workflow path determination

### Related Agents

- Gilliam (BMAD Master orchestration)
- Product Manager (planning)
- Architect (solutioning)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Initialization

🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: 'project initialization BMAD setup [PROJECT_NAME]',
  group_id: '[current-project]', // e.g., "diff-driven-saas"
})
```

**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Similar Projects: [list if any]
- Past Init Patterns: [list if any]
- Lessons Learned: [list if any]
```

**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found.
Proceeding with fresh initialization.
```

❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Initialization

**When to Log:**

- After project initialization completes
- After project level determined
- After workflow path selected
  **1. Create Project Entity:**

```javascript
create_entities({
  entities: [
    {
      name: 'Project - [project_name]',
      entityType: 'Project',
      observations: [
        'project_name: [name]',
        'project_level: [0-4]',
        'project_type: [type]',
        'workflow_path: [selected path]',
        'initialized_at: [ISO 8601]',
      ],
    },
  ],
})
```

**2. Create Event:**

```javascript
create_entities({
  entities: [
    {
      name: 'Project Initialized - [project_name]',
      entityType: 'Event',
      observations: [
        'action: initialization',
        'level: [0-4]',
        'type: [project type]',
        'timestamp: [ISO 8601]',
      ],
    },
  ],
})
```

**3. Link Project → Event:**

```javascript
create_relations({
  relations: [{ from: 'Project - [project_name]', to: '[Event name]', relationType: 'HAS_EVENT' }],
})
```

### Exit Validation (Required before completing init)

**Validation Checklist:**

---

## Integration Details

**Module:** BMM
**Phase Focus:** Initialization
**Related Workflows:**

- workflow-status (next step after init)
  **Integration Points:** Notion, Neo4j MCP
  **Platform:** Claude (via Notion AI)
