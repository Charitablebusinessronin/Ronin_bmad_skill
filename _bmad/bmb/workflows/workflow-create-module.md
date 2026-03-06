---
name: 'create-module'
slug: 'create-module'
type: 'workflow'
---

# Notion AI System Instructions: Create Module

## Workflow Identity

**Name:** create-module
**Title:** Create Module
**Module:** BMB (BMad Method Builder)
**Workflow Type:** BMAD

## Purpose

Interactive workflow to build complete BMAD modules with agents, workflows, tasks, and installation infrastructure.

## Description

Comprehensive module builder for creating complete BMAD modules. Guides through the creation of a full module including agents, workflows, tasks, and installation infrastructure. Creates properly structured modules that integrate with the BMAD Core platform.

## How to Execute This Workflow in Notion

### Activation

When you need to create a complete BMAD module:

1. **Guide through module creation** conversationally
1. **Define module structure** and purpose
1. **Create agents and workflows** for the module
1. **Set up installation infrastructure**

### Execution Steps in Notion

1. **Module Design**
1. **Component Creation**
1. **Installation Setup**

### Natural Language Commands

- “Create module” or “Build complete module”
- “Design module” or “Module builder”
- “New BMAD module” or “Module creation”

### Workflow Inputs

- Module concept or requirements
- Module brief (optional)
- Existing modules (reference)

### Workflow Outputs

- Complete module structure in Notion
- Module documentation
- Installation configuration

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
  query: 'module creation BMAD structure agents workflows [MODULE_NAME]',
  group_id: '[current-project]', // e.g., "diff-driven-saas"
})
```

**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Relevant Insights: [list titles]
- Past Module Patterns: [list if any]
- Known Issues: [list if any]
```

**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this module creation.
Proceeding without insights from past sessions.
Risk: May repeat previous module design mistakes.
```

❌ DO NOT proceed until memory retrieval completes
❌ DO NOT skip this step even if user says "just start"
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Workflow Completion

**When to Log:**

- After creating new module successfully
- After module validation completes
- When module pattern is reusable
- When module architecture decision is made
  **1. Create Event:**

```javascript
create_entities({
  entities: [
    {
      name: 'Module Created - [module_name]',
      entityType: 'Event',
      observations: [
        'module_name: [name]',
        'module_code: [code]',
        'agents_included: [list]',
        'workflows_included: [list]',
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
      name: 'Outcome - [Success/Fail] - [module_name]',
      entityType: 'Outcome',
      observations: [
        'status: [Success/Fail]',
        'module_validated: [true/false]',
        'components_count: [agents + workflows]',
        'installation_ready: [true/false]',
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
      name: 'Insight - Module Pattern - [pattern_name]',
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
  query: 'module creation [module_name] today',
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

- create-agent (for module agents)
- create-workflow (for module workflows)
  **Integration Points:** Notion, Neo4j MCP
  **Platform:** Claude (via Notion AI)
