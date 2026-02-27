# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is a **BMAD (Breakthrough Method for AI-assisted Development) agent system** — a multi-agent framework for AI-assisted product development. It is configuration-based, not code-based: there is no build step, no `npm install`, and no test runner. Everything runs through Claude Code slash commands and agent workflows.

## Module Architecture

BMAD is organized into 5 modules under `_bmad/`:

| Module | Path | Purpose |
|--------|------|---------|
| **core** | `_bmad/core/` | Foundation: BMAD Master agent, help routing, party-mode |
| **bmm** | `_bmad/bmm/` | Business/Product lifecycle: analysts, architects, devs, PM, QA, UX |
| **bmb** | `_bmad/bmb/` | Builder: create/edit/validate agents, modules, workflows |
| **cis** | `_bmad/cis/` | Creative Intelligence Suite: brainstorming, design thinking, storytelling |
| **tea** | `_bmad/tea/` | Test Architecture: ATDD, risk-based testing, CI/CD pipeline setup |

Module versions and sources are tracked in `_bmad/_config/manifest.yaml`.

## Agent Architecture

Each agent is a Markdown/YAML file in `_bmad/*/agents/`. All agents follow the same 9-step **Activation Protocol** on initialization:

1. Load persona from agent file
2. Load module `config.yaml` (critical — must succeed before proceeding)
3. Store config variables in session
4. Greet user by name (from config)
5. Display numbered menu
6. Wait for input (number, fuzzy match, or free text)
7. Process selection
8. Handle menu item attributes (`exec`, `workflow`, `action`, `data`)
9. Enforce communication style and language rules

Agents can be customized non-destructively via `_bmad/_config/agents/*.customize.yaml` (override persona, append menu items, add persistent memories).

## Workflow Architecture

Workflows live in `_bmad/*/workflows/*/`. Each workflow uses a **step-file architecture**:

- Each step is in its own file (`workflow.md`, step subdirectories `steps-c/`, `steps-e/`, `steps-v/`)
- Steps are loaded **just-in-time** — never load multiple step files at once
- Execute sections **in order**, never skip or optimize
- Track state in frontmatter `stepsCompleted` array
- Always halt at menus and wait for user input before proceeding

## BMM Development Phases

The BMM module follows 4 sequential phases:

```
Phase 1: Analysis    → Product Brief, Domain/Market/Technical Research
Phase 2: Planning    → PRD, UX Design, Validation
Phase 3: Solutioning → Architecture, Epics & Stories, Readiness Check
Phase 4: Implementation → Sprint Planning, Dev Story, Code Review, Retrospective
```

Quick path for small changes: `/bmad-bmm-quick-spec` → `/bmad-bmm-quick-dev`

## Configuration

User settings per module:

- **Global:** `_bmad/_config/` (user name: Ronin, language: English)
- **BMM:** `_bmad/bmm/config.yaml` — project name, skill level, artifact paths
- **BMB:** `_bmad/bmb/config.yaml` — output folder for created agents/modules/workflows
- **TEA:** `_bmad/tea/config.yaml` — test framework, CI platform (both auto-detect), risk threshold

## Output Directories

All artifacts are saved to `_bmad-output/`:

- `planning-artifacts/` — PRDs, UX designs, architecture docs
- `implementation-artifacts/` — code and deliverables
- `test-artifacts/` — test plans, reviews, traceability matrices
- `bmb-creations/` — newly created agents, modules, workflows

## Key Slash Commands

**Entry points:**
- `/bmad-agent-bmad-master` — unified menu routing to all agents
- `/bmad-help` — context-aware routing based on current workflow state

**BMM lifecycle:**
- `/bmad-bmm-create-product-brief`, `/bmad-bmm-create-prd`, `/bmad-bmm-create-architecture`
- `/bmad-bmm-create-epics-and-stories`, `/bmad-bmm-create-story`, `/bmad-bmm-dev-story`
- `/bmad-bmm-sprint-planning`, `/bmad-bmm-sprint-status`, `/bmad-bmm-code-review`

**Builder (BMB):**
- `/bmad-bmb-create-agent`, `/bmad-bmb-create-workflow`, `/bmad-bmb-create-module`
- `/bmad-bmb-validate-agent`, `/bmad-bmb-validate-workflow`

**Creative (CIS):**
- `/bmad-cis-brainstorming`, `/bmad-cis-design-thinking`, `/bmad-cis-innovation-strategy`

**Testing (TEA):**
- `/bmad-tea-testarch-framework`, `/bmad-tea-testarch-atdd`, `/bmad-tea-testarch-test-design`

## Persistent Memory

Two agents use sidecars in `_bmad/_memory/` to persist preferences across sessions:

- **Storyteller** (`storyteller-sidecar/`) — tracks story preferences and history
- **Tech Writer** (`tech-writer-sidecar/`) — enforces documentation standards (CommonMark strict, active voice, present tense, no time estimates)

## External Integrations

Credentials in `.env`:
- **Notion** — document storage
- **Tavily** — web search for research workflows
- **Neo4j** — memory graph

IDE integrations configured for Claude Code, Antigravity, and OpenCode.
