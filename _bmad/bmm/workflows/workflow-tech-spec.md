---
name: "tech-spec"
slug: "tech-spec"
type: "workflow"
---


# Notion AI System Instructions: Tech Spec

## Workflow Identity
**Name:** tech-spec
**Title:** Technical Specification
**Module:** BMM (Business Method Module)
**Workflow Type:** BMAD

## Purpose
Generate a comprehensive Technical Specification from PRD and Architecture with acceptance criteria and traceability mapping.

## Description
Detailed technical specification workflow that creates comprehensive technical documentation for epic-level implementation. Incorporates PRD requirements, architecture decisions, UX design, and creates acceptance criteria with full traceability to requirements.

## How to Execute This Workflow in Notion

### Activation
When you need to create a technical specification for an epic:
1. **Review inputs** (PRD, Architecture, UX Design, Epic)
1. **Guide through tech spec creation** conversationally
1. **Create structured tech spec** in Notion pages
1. **Document acceptance criteria** with traceability

### Execution Steps in Notion
1. **Context Review**
1. **Technical Specification**
1. **Traceability**

### Natural Language Commands
- “Create tech spec” or “Technical specification”
- “Generate tech spec for epic” or “Write tech spec”
- “Document technical approach” or “Tech spec”

### Workflow Inputs
- PRD (required)
- Architecture (required)
- UX Design (optional)
- Epic (specific epic for this tech spec)

### Workflow Outputs
- Technical specification document in Notion
- Acceptance criteria with traceability
- Technical approach documentation

### Related Agents
- Architect (primary)
- Developer (implementation reference)
- Scrum Master (story preparation)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Tech Spec Creation
🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: "tech spec technical specification [EPIC_NAME] architecture implementation",
  group_id: "[current-project]" // e.g., "diff-driven-saas"
})
```
**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Architecture Decisions: [list if any]
- Past Tech Specs: [list if any]
- Technical Constraints: [list if any]
```
**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this tech spec.
Proceeding without insights from past sessions.
```
❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Tech Spec Completion
**When to Log:**
- After tech spec document created
- After acceptance criteria defined
- When technical approach finalized
- When traceability mapping completed
**1. Create Event:**

```javascript
create_entities({
  entities: [{
    name: "Tech Spec Created - [epic_name]",
    entityType: "Event",
    observations: [
      "epic: [name]",
      "tech_spec_version: [version]",
      "acceptance_criteria_count: [N]",
      "technical_approach: [summary]",
      "timestamp: [ISO 8601]"
    ]
  }]
})
```
**2. Create Outcome:**

```javascript
create_entities({
  entities: [{
    name: "Outcome - Tech Spec - [epic_name]",
    entityType: "Outcome",
    observations: [
      "status: [Success/Draft/Needs Review]",
      "prd_traceability: [complete/partial]",
      "ready_for_stories: [true/false]",
      "technical_risks: [list]"
    ]
  }]
})
```
**3. Create Insight (if pattern learned):**

```javascript
create_entities({
  entities: [{
    name: "Insight - Tech Spec Pattern - [pattern_name]",
    entityType: "Insight",
    observations: [
      "pattern: [description]",
      "applicability: [epic type/domain]",
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

### Exit Validation (Required before completing tech spec)
**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before completing tech spec workflow

---

## Integration Details
**Module:** BMM
**Phase Focus:** Implementation (Phase 4)
**Related Workflows:**
- prd (input)
- architecture (input)
- create-story (uses tech spec)
**Integration Points:** Notion, Neo4j MCP
**Platform:** Claude (via Notion AI)
