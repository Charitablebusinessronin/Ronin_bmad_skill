---
name: "dev-story"
slug: "dev-story"
type: "workflow"
---


# Notion AI System Instructions: Dev Story

## Workflow Identity
**Name:** dev-story
**Title:** Develop Story
**Module:** BMM (Business Method Module)
**Workflow Type:** BMAD

## Purpose
Execute a story by implementing tasks/subtasks, writing tests, validating, and updating the story file per acceptance criteria.

## Description
Implementation workflow that executes a user story by implementing all tasks and subtasks, writing comprehensive tests, validating against acceptance criteria, and updating the story status. Ensures complete test coverage and adherence to all acceptance criteria before marking complete.

## How to Execute This Workflow in Notion

### Activation
When you need to implement a user story:
1. **Load story context** from Notion
1. **Review acceptance criteria** and requirements
1. **Implement tasks** systematically
1. **Write and run tests**
1. **Validate completion**

### Execution Steps in Notion
1. **Story Context Review**
1. **Implementation**
1. **Testing and Validation**

### Natural Language Commands
- “Develop story” or “Implement story”
- “Execute story” or “Work on story”
- “Implement user story” or “Code story”

### Workflow Inputs
- Story document (required)
- Story context (required)
- Architecture and tech spec (reference)

### Workflow Outputs
- Implemented code
- Test suite
- Updated story status
- Completion documentation

### Related Agents
- Developer (primary)
- Test Architect (testing guidance)
- Scrum Master (process)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Story Implementation
🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: "story implementation [STORY_ID] code patterns blockers",
  group_id: "[current-project]" // e.g., "diff-driven-saas"
})
```
**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Related Stories: [list if any]
- Code Patterns: [list if any]
- Known Blockers: [list if any]
```
**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this story.
Proceeding without insights from past sessions.
```
❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Story Implementation
**When to Log:**
- After story implementation completed
- After tests written and passing
- After acceptance criteria validated
- When blocker encountered and resolved
**1. Create Event:**

```javascript
create_entities({
  entities: [{
    name: "Story Implemented - [story_id]",
    entityType: "Event",
    observations: [
      "story_id: [id]",
      "story_title: [title]",
      "tasks_completed: [N]",
      "tests_written: [N]",
      "acceptance_criteria_met: [N/total]",
      "timestamp: [ISO 8601]"
    ]
  }]
})
```
**2. Create Outcome:**

```javascript
create_entities({
  entities: [{
    name: "Outcome - Story - [story_id]",
    entityType: "Outcome",
    observations: [
      "status: [Complete/Blocked/Needs Review]",
      "all_tests_passing: [true/false]",
      "all_ac_met: [true/false]",
      "blockers_encountered: [list or none]",
      "code_quality: [assessment]"
    ]
  }]
})
```
**3. Create Insight (if pattern learned):**

```javascript
create_entities({
  entities: [{
    name: "Insight - Dev Pattern - [pattern_name]",
    entityType: "Insight",
    observations: [
      "pattern: [description]",
      "code_location: [files/modules]",
      "reusability: [high/medium/low]"
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

### Exit Validation (Required before completing story)
**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before marking story complete

---

## Integration Details
**Module:** BMM
**Phase Focus:** Implementation (Phase 4)
**Related Workflows:**
- create-story (input)
- story-done (next step)
- code-review (validation)
**Integration Points:** Notion, Neo4j MCP
**Platform:** Claude (via Notion AI)
