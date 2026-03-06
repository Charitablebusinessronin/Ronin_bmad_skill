---
name: 'party-mode'
slug: 'party-mode'
type: 'workflow'
---

# Notion AI System Instructions: Party Mode

## Workflow Identity

**Name:** party-mode
**Title:** Party Mode - Multi-Agent Group Discussion
**Module:** CORE
**Workflow Type:** BMAD

## Purpose

Orchestrates group discussions between all installed BMAD agents, enabling natural multi-agent conversations.

## Description

Unique workflow that enables group discussions between multiple BMAD agents simultaneously. Allows natural multi-agent conversations where different agents can contribute their expertise to discussions, brainstorming, or problem-solving sessions. Creates a collaborative agent environment.

## How to Execute This Workflow in Notion

### Activation

When you want to engage multiple agents in a group discussion:

1. **Initialize party mode** session in Notion
1. **Invite relevant agents** to the conversation
1. **Facilitate multi-agent discussion**
1. **Capture conversation** and outcomes

### Execution Steps in Notion

1. **Session Initialization**
1. **Multi-Agent Facilitation**
1. **Outcome Documentation**

### Natural Language Commands

- “Start party mode” or “Group chat with agents”
- “Multi-agent discussion” or “Agent collaboration”
- “Party mode” or “Group agent session”

### Workflow Inputs

- Discussion topic or goal
- Agent manifest (available agents)

### Workflow Outputs

- Multi-agent conversation transcript in Notion
- Collaborative insights and decisions
- Summary of agent contributions

### Related Agents

- Gilliam (BMAD Master orchestration)
- All BMAD agents (participants)

## Primary Agent Participants

- Winston (Architect) - System architecture and technical design
- Brooks (Data-First Strategist) - Data model and structural integrity
- Troy (Developer) - Implementation and automation
- Allura (UX Designer) - User experience and design

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Party Mode Start

🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: 'party mode multi-agent discussion [TOPIC] collaboration',
  group_id: '[current-project]', // e.g., "diff-driven-saas"
})
```

**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Previous Discussions: [list titles]
- Agent Contributions: [list if any]
- Unresolved Questions: [list if any]
```

**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this topic.
Proceeding without insights from past sessions.
```

❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Party Mode Session

**When to Log:**

- After multi-agent discussion completes
- When consensus reached on topic
- When key decision made by agents
- When novel insight discovered
  **1. Create Event:**

```javascript
create_entities({
  entities: [
    {
      name: 'Party Mode - [topic_summary]',
      entityType: 'Event',
      observations: [
        'topic: [discussion topic]',
        'agents_participated: [list]',
        'duration: [estimate]',
        'key_decisions: [list]',
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
      name: 'Outcome - Party Mode - [topic]',
      entityType: 'Outcome',
      observations: [
        'consensus_reached: [true/false]',
        'decisions: [list]',
        'action_items: [list]',
        'dissenting_views: [if any]',
      ],
    },
  ],
})
```

**3. Create Insight (if breakthrough discovered):**

```javascript
create_entities({
  entities: [
    {
      name: 'Insight - Multi-Agent - [insight_name]',
      entityType: 'Insight',
      observations: [
        'insight: [description]',
        'contributing_agents: [list]',
        'applicability: [when to use]',
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

### Exit Validation (Required before ending session)

**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before ending session

---

## Integration Details

**Module:** CORE
**Phase Focus:** Collaboration
**Related Workflows:**

- brainstorming (can use party mode)
- problem-solving (multi-agent approach)
  **Integration Points:** Notion, Neo4j MCP
  **Platform:** Claude (via Notion AI)
  Session initialized for multi-agent meeting discussion.
  Agents invited: Brooks, Winston, Allura, Troy
  Topic: Meeting discussion and collaboration
  === Build Completion Discussion ===
  ✅ Next.js build succeeded after fixing:
- TypeScript config: excluded package/ directory, added allowImportingTsExtensions
- Routing conflicts resolved
- CSS imports fixed
  ⚠️ Known issues:
- Payload type generation has ESM compatibility issues (non-blocking)
- Dev server startup command needs syntax fix
