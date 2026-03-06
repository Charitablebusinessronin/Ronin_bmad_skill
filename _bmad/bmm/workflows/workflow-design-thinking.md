---
name: "design-thinking"
slug: "design-thinking"
type: "workflow"
---


# Notion AI System Instructions: Design Thinking

## Workflow Identity
**Name:** design-thinking
**Title:** Design Thinking Workflow
**Module:** CIS (Creative Innovation System)
**Workflow Type:** BMAD

## Purpose
Guide human-centered design processes using empathy-driven methodologies. Walk through design thinking phases - Empathize, Define, Ideate, Prototype, and Test - to create solutions deeply rooted in user needs.

## Description
Comprehensive design thinking workflow that guides users through the five phases of design thinking: Empathize, Define, Ideate, Prototype, and Test. Focuses on human-centered design with empathy at the core, ensuring solutions are deeply rooted in user needs and validated through real user interaction.

## How to Execute This Workflow in Notion

### Activation
When you need to apply design thinking to create user-centered solutions:
1. **Guide through design thinking phases** conversationally
1. **Facilitate empathy and user research**
1. **Create design artifacts** in Notion
1. **Document design process** and decisions

### Execution Steps in Notion
1. **Empathize Phase**
1. **Define Phase**
1. **Ideate Phase**
1. **Prototype Phase**
1. **Test Phase**

### Natural Language Commands
- “Design thinking” or “Human-centered design”
- “Apply design thinking” or “Design process”
- “Empathy-driven design” or “User-centered design”

### Workflow Inputs
- Design context (optional)
- User research (optional)

### Workflow Outputs
- Design thinking process documentation in Notion
- Empathy maps and user personas
- Prototypes and test results
- Refined solutions

### Related Agents
- Design Thinking Coach (primary)
- UX Designer (design execution)
- Innovation Strategist (strategic design)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Design Thinking
🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: "design thinking empathy user research [USER_GROUP/DOMAIN]",
  group_id: "[current-project]" // e.g., "diff-driven-saas"
})
```
**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- User Insights: [list if any]
- Previous Personas: [list if any]
- Tested Prototypes: [list if any]
```
**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this user group.
Proceeding without insights from past sessions.
```
❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Design Thinking
**When to Log:**
- After each phase completed (Empathize/Define/Ideate/Prototype/Test)
- When user insight discovered
- When prototype tested with users
- When solution validated
**1. Create Event:**

```javascript
create_entities({
  entities: [{
    name: "Design Thinking - [phase] - [project]",
    entityType: "Event",
    observations: [
      "phase: [Empathize/Define/Ideate/Prototype/Test]",
      "user_group: [target users]",
      "key_activity: [what was done]",
      "artifacts_created: [list]",
      "timestamp: [ISO 8601]"
    ]
  }]
})
```
**2. Create Outcome:**

```javascript
create_entities({
  entities: [{
    name: "Outcome - Design Thinking - [phase]",
    entityType: "Outcome",
    observations: [
      "status: [Complete/Needs Iteration]",
      "user_validated: [true/false]",
      "key_findings: [list]",
      "next_phase_ready: [true/false]"
    ]
  }]
})
```
**3. Create Insight (user insight):**

```javascript
create_entities({
  entities: [{
    name: "Insight - User - [insight_name]",
    entityType: "Insight",
    observations: [
      "user_need: [description]",
      "evidence: [how discovered]",
      "design_implication: [what it means for design]"
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

### Exit Validation (Required before completing phase)
**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before completing phase

---

## Integration Details
**Module:** CIS
**Phase Focus:** Creative Innovation
**Related Workflows:**
- brainstorming (ideation phase)
- problem-solving (problem definition)
**Integration Points:** Notion, Neo4j MCP
**Platform:** Claude (via Notion AI)
