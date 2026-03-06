---
name: "create-epics-and-stories"
slug: "create-epics-stories"
type: "workflow"
---


# Notion AI System Instructions: Create Epics and Stories

## Workflow Identity
**Name:** create-epics-and-stories
**Title:** Epic and Story Decomposition
**Module:** BMM (Business Method Module)
**Workflow Type:** BMAD

## Purpose
Transform PRD requirements into bite-sized stories organized in epics for 200k context dev agents.

## Description
Systematic workflow that breaks down PRD requirements into manageable epics and user stories. Optimized for creating stories that fit within 200k token context windows for development agents, ensuring each story is appropriately scoped and contains all necessary context.

## How to Execute This Workflow in Notion

### Activation
When you need to decompose PRD requirements into implementable epics and stories:
1. **Review PRD** from Notion pages
1. **Guide through epic creation** conversationally
1. **Create epics database** in Notion
1. **Break epics into stories** with proper structure

### Execution Steps in Notion
1. **Epic Creation**
1. **Story Decomposition**
1. **Validation**

### Natural Language Commands
- “Create epics and stories” or “Break down PRD”
- “Decompose requirements” or “Generate epics”
- “Create user stories” or “Story breakdown”

### Workflow Inputs
- PRD document (required)
- Product brief (optional context)
- Domain brief (optional context)

### Workflow Outputs
- Epics database in Notion
- User stories linked to epics
- Traceability to PRD requirements

### Related Agents
- Product Manager (primary)
- Scrum Master (story preparation)
- Business Analyst (requirements)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Epic/Story Creation
🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: "epic story decomposition [PROJECT_NAME] requirements breakdown",
  group_id: "[current-project]" // e.g., "diff-driven-saas"
})
```
**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Previous Epics: [list if any]
- Story Patterns: [list if any]
- Sizing Insights: [list if any]
```
**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found.
Proceeding without insights from past sessions.
```
❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Epic/Story Creation
**When to Log:**
- After epics created from PRD
- After stories decomposed from epics
- When story sizing completed
- When traceability established
**1. Create Event:**

```javascript
create_entities({
  entities: [{
    name: "Epics & Stories Created - [project_name]",
    entityType: "Event",
    observations: [
      "project: [name]",
      "epics_count: [N]",
      "stories_count: [N]",
      "prd_coverage: [percentage]",
      "timestamp: [ISO 8601]"
    ]
  }]
})
```
**2. Create Outcome:**

```javascript
create_entities({
  entities: [{
    name: "Outcome - Decomposition - [project_name]",
    entityType: "Outcome",
    observations: [
      "status: [Success/Partial]",
      "stories_ready_for_dev: [N]",
      "context_window_compliant: [true/false]",
      "traceability_complete: [true/false]"
    ]
  }]
})
```
**3. Create Insight (if pattern learned):**

```javascript
create_entities({
  entities: [{
    name: "Insight - Decomposition Pattern - [pattern_name]",
    entityType: "Insight",
    observations: [
      "pattern: [description]",
      "optimal_story_size: [guidance]",
      "benefits: [why it works]"
    ]
  }]
})
```
**4. Link Event → Outcome → Insight:**

```javascript
create_relations({
  relations: [
    { from: "[Event name]", to: "[Outcome name]", relationType: "RESULTED_IN" },
    { from: "[Outcome name]", to: "[Insight name]", relationType: "INFORMED" }
  ]
})
```

### Exit Validation (Required before completing decomposition)
**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before completing decomposition workflow

---

## Integration Details
**Module:** BMM
**Phase Focus:** Planning (Phase 2)
**Related Workflows:**
- prd (input)
- create-story (uses epics)
- architecture (after epics)
**Integration Points:** Notion, Neo4j MCP
**Platform:** Claude (via Notion AI)
