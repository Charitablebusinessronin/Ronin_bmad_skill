# AGENTS.md - BMAD Agent System

## Project Overview

This is a **BMAD (Breakthrough Method for AI-assisted Development)** agent system — a multi-agent framework for AI-assisted product development. It is **configuration-based, not code-based**: there is no build step, no `npm install`, and no test runner. Everything runs through Claude Code slash commands and agent workflows.

## Build/Lint/Test Commands

**This project has no build, lint, or test commands.** It is a pure Markdown/YAML configuration system.

- No `package.json` build scripts exist
- No tests to run
- No linting required
- Agents and workflows are defined in `_bmad/` as Markdown/YAML files

### Output Artifacts

All artifacts are saved to `_bmad-output/`:

| Directory | Purpose |
|-----------|---------|
| `_bmad-output/planning-artifacts/` | PRDs, UX designs, architecture docs |
| `_bmad-output/implementation-artifacts/` | Code and deliverables |
| `_bmad-output/test-artifacts/` | Test plans, reviews, traceability matrices |
| `_bmad-output/bmb-creations/` | Newly created agents, modules, workflows |

---

## Code Style Guidelines

### Architecture Overview

BMAD is organized into 5 modules under `_bmad/`:

| Module | Path | Purpose |
|--------|------|---------|
| **core** | `_bmad/core/` | Foundation: BMAD Master agent, help routing, party-mode |
| **bmm** | `_bmad/bmm/` | Business/Product lifecycle: analysts, architects, devs, PM, QA, UX |
| **bmb** | `_bmad/bmb/` | Builder: create/edit/validate agents, modules, workflows |
| **cis** | `_bmad/cis/` | Creative Intelligence Suite: brainstorming, design thinking, storytelling |
| **tea** | `_bmad/tea/` | Test Architecture: ATDD, risk-based testing, CI/CD pipeline setup |

### File Formats

- **Agents**: Markdown (`.md`) files in `_bmad/*/agents/`
- **Workflows**: Markdown/YAML in `_bmad/*/workflows/*/`
- **Configs**: YAML (`.yaml`) in `_bmad/*/config.yaml` and `_bmad/_config/`
- **Customizations**: YAML in `_bmad/_config/agents/*.customize.yaml`

### Agent Activation Protocol

All agents follow the same 9-step **Activation Protocol** on initialization:

1. Load persona from agent file
2. Load module `config.yaml` (must succeed before proceeding)
3. Store config variables in session
4. Greet user by name (from config)
5. Display numbered menu
6. Wait for input (number, fuzzy match, or free text)
7. Process selection
8. Handle menu item attributes (`exec`, `workflow`, `action`, `data`)
9. Enforce communication style and language rules

### Workflow Architecture

Workflows use a **step-file architecture**:

- Each step is in its own file
- Steps are loaded **just-in-time** — never load multiple step files at once
- Execute sections **in order**, never skip or optimize
- Track state in frontmatter `stepsCompleted` array
- Always halt at menus and wait for user input before proceeding

### Agent File Structure

Agent files use YAML frontmatter with these sections:

```yaml
---
name: "agent-name"
description: "Agent description"
---
<agent xml with activation, persona, menu>
```

### Menu Item Attributes

| Attribute | Purpose |
|-----------|---------|
| `workflow` | Path to workflow YAML to execute |
| `exec` | Path to executable Markdown |
| `action` | Direct action to perform |
| `data` | Data to pass to handler |

### Naming Conventions

- Agent files: ` kebab-case.md` (e.g., `dev.md`, `quick-flow-solo-dev.md`)
- Workflows: `workflow.yaml` or `workflow.md`
- Steps: `step-NN-*.md` pattern
- Config files: `config.yaml`
- Customizations: `{agent-name}.customize.yaml`

### Communication Style

Per agent config (`_bmad/bmm/config.yaml`):

- User name: **Ronin**
- Communication language: **English**
- Document output: **English chill relaxed**

### Error Handling

- **Config loading failure**: STOP and report error — do not proceed
- **Workflow not implemented**: Inform user with "workflow hasn't been implemented yet"
- **Menu match failures**: "Not recognized" message, allow retry
- **Multiple fuzzy matches**: Ask user to clarify

### Best Practices

1. **Never break character** — stay in agent persona until exit command
2. **Load configs first** — verify config.yaml loads before proceeding
3. **Execute workflows in order** — no skipping steps
4. **Save after each workflow step** — never batch multiple steps
5. **Use fuzzy matching** for menu items — case-insensitive substring match
6. **Document decisions** — update story files with implementation notes

### Key Slash Commands

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

### External Integrations

Credentials in `.env`:
- **Notion** — document storage
- **Tavily** — web search for research workflows
- **Neo4j** — memory graph

### Module Versions

Module versions and sources are tracked in `_bmad/_config/manifest.yaml`.

### IDE Integrations

Configured for Claude Code, Antigravity, and OpenCode (see `_bmad/_config/ides/`).
