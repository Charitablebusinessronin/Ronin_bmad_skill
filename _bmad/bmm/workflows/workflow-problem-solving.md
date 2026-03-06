---
name: "problem-solving"
slug: "problem-solving"
type: "workflow"
---


# Notion AI System Instructions: Problem Solving

## Workflow Identity
**Name:** problem-solving
**Title:** Problem Solving Workflow
**Module:** CIS (Creative Innovation System)
**Workflow Type:** BMAD

## Purpose
Apply systematic problem-solving methodologies to crack complex challenges. Guide through problem diagnosis, root cause analysis, creative solution generation, evaluation, and implementation planning using proven frameworks.

## Description
Systematic problem-solving workflow that guides through comprehensive problem-solving methodologies including TRIZ, Theory of Constraints, Systems Thinking, and Root Cause Analysis. Combines divergent and convergent thinking to understand problems fully before narrowing toward solutions. Focuses on root causes, not symptoms.

## How to Execute This Workflow in Notion

### Activation
When you need to solve a complex problem systematically:
1. **Guide through problem-solving process** conversationally
1. **Apply systematic methodologies**
1. **Document analysis and solutions** in Notion
1. **Create implementation plan**

### Execution Steps in Notion
1. **Problem Diagnosis**
1. **Root Cause Analysis**
1. **Solution Generation**

### Natural Language Commands
- “Solve problem” or “Systematic problem solving”
- “Root cause analysis” or “Find root cause”
- “Apply problem-solving” or “Problem-solving methodology”

### Workflow Inputs
- Problem context (optional)
- Previous solution attempts (optional)

### Workflow Outputs
- Problem analysis document in Notion
- Root cause analysis
- Solution design and evaluation
- Implementation plan

### Related Agents
- Problem Solver (primary)
- Innovation Strategist (strategic solutions)
- Design Thinking Coach (user-focused solutions)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Problem Solving
🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: "problem solving root cause [PROBLEM_DOMAIN] solutions",
  group_id: "[current-project]" // e.g., "diff-driven-saas"
})
```
**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Similar Problems: [list if any]
- Past Solutions: [list if any]
- Root Cause Patterns: [list if any]
```
**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this problem domain.
Proceeding without insights from past sessions.
```
❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Problem Solving
**When to Log:**
- After problem diagnosis completed
- After root cause identified
- After solution designed
- When implementation plan created
**1. Create Event:**

```javascript
create_entities({
  entities: [{
    name: "Problem Solved - [problem_summary]",
    entityType: "Event",
    observations: [
      "problem: [description]",
      "methodology: [TRIZ/ToC/Systems Thinking/RCA]",
      "root_cause: [identified cause]",
      "solution: [selected approach]",
      "timestamp: [ISO 8601]"
    ]
  }]
})
```
**2. Create Outcome:**

```javascript
create_entities({
  entities: [{
    name: "Outcome - Problem - [problem_summary]",
    entityType: "Outcome",
    observations: [
      "status: [Solved/Partially Solved/Needs More Analysis]",
      "root_cause_confidence: [high/medium/low]",
      "solution_validated: [true/false]",
      "implementation_ready: [true/false]"
    ]
  }]
})
```
**3. Create Insight (problem-solving pattern):**

```javascript
create_entities({
  entities: [{
    name: "Insight - Problem Pattern - [pattern_name]",
    entityType: "Insight",
    observations: [
      "problem_type: [category]",
      "effective_methodology: [what worked]",
      "reusable_solution: [description]"
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

### Exit Validation (Required before completing problem solving)
**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before completing problem-solving workflow

---

## Integration Details
**Module:** CIS
**Phase Focus:** Creative Innovation
**Related Workflows:**
- design-thinking (problem definition)
- innovation-strategy (strategic problems)
**Integration Points:** Notion, Neo4j MCP
**Platform:** Claude (via Notion AI)
