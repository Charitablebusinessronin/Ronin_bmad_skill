---
name: "prd"
slug: "prd"
type: "workflow"
---


# Notion AI System Instructions: PRD (Product Requirements Document)

## Workflow Identity
**Name:** prd
**Title:** Product Requirements Document
**Module:** BMM (Business Method Module)
**Workflow Type:** BMAD

## Purpose
Unified PRD workflow for project levels 2-4. Produces strategic PRD and tactical epic breakdown. Hands off to architecture workflow for technical design.

## Description
Comprehensive workflow for creating Product Requirements Documents for medium to large projects (Levels 2-4). Produces a strategic PRD with functional requirements, non-functional requirements, and breaks down requirements into implementable epics. Note: Level 0-1 projects use tech-spec workflow instead.

## How to Execute This Workflow in Notion

### Activation
When you need to create a Product Requirements Document for a Level 2-4 project:
1. **Review inputs** from Notion (product brief, market research, etc.)
1. **Guide through PRD creation** conversationally
1. **Create structured PRD** in Notion pages
1. **Break down into epics** and create epic database

### Execution Steps in Notion
1. **Requirements Gathering**
1. **PRD Creation**
1. **Epic Breakdown**

### Natural Language Commands
- “Create PRD” or “Product requirements document”
- “Write PRD” or “Generate product requirements”
- “Break down into epics” or “Create epics”

### Workflow Inputs
- Product brief (from product-brief workflow)
- Market research (from research workflow)
- Domain brief (optional)

### Workflow Outputs
- PRD document in Notion
- Epics database with linked requirements
- Requirements traceability structure

### Related Agents
- Product Manager (primary)
- Business Analyst (support)
- UX Designer (user requirements)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before PRD Creation
🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: "PRD requirements product [PROJECT_NAME] features priorities",
  group_id: "[current-project]" // e.g., "diff-driven-saas"
})
```
**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Previous Requirements: [list if any]
- Past PRD Patterns: [list if any]
- Stakeholder Feedback: [list if any]
```
**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this PRD.
Proceeding without insights from past sessions.
```
❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After PRD Completion
**When to Log:**
- After PRD document created
- After requirements prioritized
- After epic breakdown completed
- When key product decision made
**1. Create Event:**

```javascript
create_entities({
  entities: [{
    name: "PRD Created - [project_name]",
    entityType: "Event",
    observations: [
      "project: [name]",
      "prd_version: [version]",
      "functional_requirements_count: [N]",
      "non_functional_requirements_count: [N]",
      "epics_count: [N]",
      "timestamp: [ISO 8601]"
    ]
  }]
})
```
**2. Create Outcome:**

```javascript
create_entities({
  entities: [{
    name: "Outcome - PRD - [project_name]",
    entityType: "Outcome",
    observations: [
      "status: [Success/Draft/Needs Review]",
      "stakeholder_approved: [true/false]",
      "ready_for_architecture: [true/false]",
      "key_features: [list]"
    ]
  }]
})
```
**3. Create Insight (if pattern learned):**

```javascript
create_entities({
  entities: [{
    name: "Insight - PRD Pattern - [pattern_name]",
    entityType: "Insight",
    observations: [
      "pattern: [description]",
      "applicability: [domain/project type]",
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

### Exit Validation (Required before completing PRD)
**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before completing PRD workflow

---

## Integration Details
**Module:** BMM
**Phase Focus:** Planning (Phase 2)
**Related Workflows:**
- product-brief (input)
- create-epics-and-stories (next step)
- architecture (after PRD)
**Integration Points:** Notion, Neo4j MCP
**Platform:** Claude (via Notion AI)
