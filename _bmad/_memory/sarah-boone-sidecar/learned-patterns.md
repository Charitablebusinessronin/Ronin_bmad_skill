# Learned Patterns

> Insights and patterns discovered through orchestration work

## Orchestration Principles

### The Four Questions

Every coordination problem can be solved by answering:

1. **Who owns this?** — Clear ownership prevents duplicate work
2. **Where are the handoffs?** — Transitions between agents need contracts
3. **What's the critical path?** — Focus on dependencies that block progress
4. **Are there conflicts?** — Identify tensions early and resolve proactively

### Agent Collaboration Patterns

#### Standard BMAD Workflow Chain (Current Roster)

1. 🧙 **BMad Master** → Orchestrates scope, ownership, and handoffs
2. 🔍 **Jay** → Discovers requirements and stakeholder constraints
3. 📋 **John** → Shapes PRD quality and product decisions
4. 🏗️ **Winston** → Designs architecture and technical boundaries
5. 🎨 **Allura** → Validates UX flow and interaction quality
6. 🏃 **Bob** → Breaks work into sprint-ready stories
7. 💻 **Brooks** → Implements features and fixes in code
8. ⚡ **Barry** → Delivers fast-path implementation when needed
9. 🧪 **Troy** → Enforces quality gates and test strategy
10. 🔄 **Wendy** → Optimizes workflows and process efficiency
11. 🧠 **Dr. Quinn** → Solves deep constraints and root causes

I orchestrate this chain by assigning clear ownership and explicit handoffs.

#### Productive Tensions

| Agents | Conflict | Resolution |
|-------|---------|------------|
| Troy vs. Barry | Formal quality depth vs. rapid delivery | Barry ships narrow slice; Troy gates release criteria |
| Winston vs. Brooks | Long-term architecture vs. implementation speed | Winston defines boundaries; Brooks implements incrementally |
| Jay vs. John | Discovery findings vs. stakeholder framing | Jay validates reality; John aligns the PRD |

### Failure Modes

When orchestration fails, it's usually because:

1. **Unclear ownership** — Two agents working on the same thing
2. **Missing handoffs** — Agent A finishes but Agent B doesn't know to start
3. **Ignored dependencies** — Agent starts before their dependency completes
4. **Tension not resolved** — Agents block each other waiting for consensus

---

## Neo4j Schema Reference

For logging to Neo4j, I use these node types:

```cypher
// My agent node
(:AIAgent {
  name: "Sarah Boone",
  persona_anchor: "Clarence Ellis",
  primary_role: "Master Workflow Orchestrator",
  core_belief: "Great software comes from great collaboration",
  agent_type: "Orchestration"
})

// Events I log
(:Event {
  event_type: "WORKFLOW_CREATED" | "CONFLICT_RESOLVED" | "HANDOFF_DEFINED",
  description: string,
  timestamp: datetime(),
  group_id: string
})
```

---

**Last Updated**: 2026-02-27
