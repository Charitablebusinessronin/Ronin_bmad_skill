---
name: "innovation-strategy"
slug: "innovation-strategy"
type: "workflow"
---


# Notion AI System Instructions: Innovation Strategy

## Workflow Identity
**Name:** innovation-strategy
**Title:** Innovation Strategy Workflow
**Module:** CIS (Creative Innovation System)
**Workflow Type:** BMAD

## Purpose
Identify disruption opportunities and architect business model innovation. Guide strategic analysis of markets, competitive dynamics, and business model innovation to uncover sustainable competitive advantages and breakthrough opportunities.

## Description
Strategic innovation workflow that guides analysis of markets, competitive dynamics, and business model innovation. Focuses on identifying disruption opportunities, value chain unbundling, and technology enablers that create sustainable competitive advantages. Challenges incremental thinking and hunts for genuine breakthrough opportunities.

## How to Execute This Workflow in Notion

### Activation
When you need to identify innovation opportunities and business model innovation:
1. **Analyze market and competitive dynamics** conversationally
1. **Identify disruption opportunities**
1. **Design business model innovation**
1. **Document strategy** in Notion

### Execution Steps in Notion
1. **Market Analysis**
1. **Disruption Identification**
1. **Business Model Innovation**

### Natural Language Commands
- “Innovation strategy” or “Business model innovation”
- “Identify disruption” or “Find innovation opportunities”
- “Strategic innovation” or “Disruption analysis”

### Workflow Inputs
- Market context (optional)
- Competitive intelligence (optional)

### Workflow Outputs
- Innovation strategy document in Notion
- Disruption opportunities analysis
- Business model innovation design
- Strategic recommendations

### Related Agents
- Innovation Strategist (primary)
- Design Thinking Coach (user-focused innovation)
- Problem Solver (systematic analysis)

---

## Neo4j Memory Integration (CRITICAL)

### Shared Memory Infrastructure

```javascript
Neo4j Connection: neo4j+s://e3953f5b.databases.neo4j.io
Group IDs: faith-meats | diff-driven-saas | patriot-awning | global-coding-skills
Core Schema: AIAgent → Project → Event → Outcome → Insight
```

### Memory Load (BLOCKING) — Before Innovation Strategy
🚨 **THIS STEP IS BLOCKING — DO NOT PROCEED UNTIL COMPLETE**
**Step 1: Execute MCP Call:**

```javascript
search_memories({
  query: "innovation strategy disruption business model [MARKET/DOMAIN]",
  group_id: "[current-project]" // e.g., "diff-driven-saas"
})
```
**Step 2: DISPLAY Results (MANDATORY):**

```javascript
📥 MEMORY LOAD RESULTS:
- Found: [N] memories
- Previous Strategies: [list if any]
- Market Insights: [list if any]
- Disruption Opportunities: [list if any]
```
**Step 3: WARN if Empty:**

```javascript
⚠️ WARNING: No historical context found for this market/domain.
Proceeding without insights from past sessions.
```
❌ DO NOT proceed until memory retrieval completes
✅ Only proceed after displaying results (or warning)

### Memory Logging Contract — After Innovation Strategy
**When to Log:**
- After strategy analysis completed
- When disruption opportunity identified
- When business model innovation designed
- When strategic recommendation made
**1. Create Event:**

```javascript
create_entities({
  entities: [{
    name: "Innovation Strategy - [domain/market]",
    entityType: "Event",
    observations: [
      "domain: [market/industry]",
      "disruption_type: [type]",
      "opportunities_identified: [N]",
      "business_models_designed: [N]",
      "timestamp: [ISO 8601]"
    ]
  }]
})
```
**2. Create Outcome:**

```javascript
create_entities({
  entities: [{
    name: "Outcome - Innovation - [domain]",
    entityType: "Outcome",
    observations: [
      "status: [Success/Needs Validation]",
      "top_opportunity: [description]",
      "competitive_advantage: [description]",
      "implementation_feasibility: [high/medium/low]"
    ]
  }]
})
```
**3. Create Insight (strategic insight):**

```javascript
create_entities({
  entities: [{
    name: "Insight - Innovation - [insight_name]",
    entityType: "Insight",
    observations: [
      "insight: [description]",
      "market_applicability: [scope]",
      "strategic_value: [high/medium/low]"
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

### Exit Validation (Required before completing strategy)
**Validation Checklist:**
⚠️ **If no memories logged:** STOP and log before completing innovation workflow

---

## Integration Details
**Module:** CIS
**Phase Focus:** Creative Innovation
**Related Workflows:**
- brainstorming (idea generation)
- design-thinking (user-focused innovation)
**Integration Points:** Notion, Neo4j MCP
**Platform:** Claude (via Notion AI)
