# Architecture Patterns

## Primary Pattern

- **Configuration-driven multi-agent orchestration**
  - Agents and workflows are authored as markdown/yaml definitions.
  - Execution follows step-file protocols and command entrypoints.

## Integration Pattern

- **MCP-first tool invocation model**
  - External systems (Neo4j, Notion, context docs) are accessed through MCP tools.
  - User preference explicitly prioritizes MCP over bespoke Python integrations.

## State Pattern

- **Graph + artifact dual persistence**
  - Neo4j stores memory and event relationships.
  - `_bmad-output/` and `docs/` store generated planning/analysis artifacts.

## Repository Pattern

- **Single-repo monolith for workflow assets**
  - Core content under `_bmad/`, command adapters under `.agent/` and `.claude/`.
  - No traditional app build/test pipeline; workflow execution is the primary runtime behavior.
