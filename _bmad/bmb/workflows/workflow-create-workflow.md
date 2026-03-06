---
name: 'create-workflow'
slug: 'create-workflow'
type: 'workflow'
---

# Notion AI System Instructions: Create Workflow

## Workflow Identity

**Name:** create-workflow
**Title:** Create Workflow
**Module:** BMB (BMad Method Builder)
**Workflow Type:** BMAD

## Purpose

Interactive workflow builder that guides creation of new BMAD workflows with proper structure and validation for optimal human-AI collaboration. Includes optional brainstorming phase for workflow ideas and design.

## Description

Comprehensive workflow builder for creating new BMAD workflows. Guides through the creation process with proper structure, instructions, templates, and validation. Includes optional brainstorming phase for workflow design and ensures compliance with BMAD Core standards for optimal human-AI collaboration.

## How to Execute This Workflow in Notion

### Activation

When you need to create a new BMAD workflow:

1. **Guide through workflow creation** conversationally
1. **Define workflow purpose** and structure
1. **Create workflow components** (instructions, templates, validation)
1. **Document workflow** in Notion

### Execution Steps in Notion

1. **Workflow Design**
1. **Structure Creation**
1. **Documentation**

### Natural Language Commands

- “Create workflow” or “Build new workflow”
- “Design workflow” or “Workflow builder”
- “New BMAD workflow” or “Workflow creation”

### Workflow Inputs

- Workflow concept or requirements
- Existing workflows (reference)
- Workflow creation guide (reference)

### Workflow Outputs

- Workflow system instructions in Notion
- Workflow documentation
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
  query: 'workflow creation BMAD structure validation [WORKFLOW_NAME]',
  group_id: '[current-project]', // e.g., "diff-driven-saas"
})
```

**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Relevant Insights: [list titles]
- Past Workflow Patterns: [list if any]
- Known Issues: [list if any]
```

**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this workflow.
Proceeding without insights from past sessions.
Risk: May repeat previous workflow design mistakes.
```

❌ DO NOT proceed until memory retrieval completes
❌ DO NOT skip this step even if user says "just start"
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Workflow Completion

**When to Log:**

- After creating new workflow successfully
- After workflow validation completes
- When workflow pattern is reusable
- When workflow design decision is made
  **1. Create Event:**

```javascript
create_entities({
  entities: [
    {
      name: 'Workflow Created - [workflow_name]',
      entityType: 'Event',
      observations: [
        'workflow_name: [name]',
        'workflow_type: BMAD',
        'module: [BMB/BMM/CIS/CORE]',
        'purpose: [one-line summary]',
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
      name: 'Outcome - [Success/Fail] - [workflow_name]',
      entityType: 'Outcome',
      observations: [
        'status: [Success/Fail]',
        'workflow_validated: [true/false]',
        'components_created: [list]',
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
      name: 'Insight - Workflow Pattern - [pattern_name]',
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
  query: 'workflow creation [workflow_name] today',
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

- create-agent (for agent workflows)
- create-module (for module workflows)
  **Integration Points:** Notion, Neo4j MCP
  **Platform:** Claude (via Notion AI)
