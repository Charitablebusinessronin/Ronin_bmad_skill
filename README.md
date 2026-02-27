# BMAD — Breakthrough Method for AI-assisted Development

> **"Build More, Architect Dreams"** — A multi-agent framework for AI-assisted product development

[![BMAD Version](https://img.shields.io/badge/BMAD-6.0.3-blue)](./_bmad/_config/manifest.yaml)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 What is BMAD?

BMAD is a **configuration-based, not code-based** agent framework. There is no build step, no `npm install`, and no test runner. Everything runs through Claude Code slash commands and agent workflows defined in Markdown/YAML.

### Core Philosophy

- **Collaboration is a protocol, not a wish**
- **Ownership must be unambiguous**
- **Handoffs must carry full context**
- **Coordination scales only when the system is designed for it**

---

## 📁 Project Structure

```
bmad/
├── _bmad/                          # Core framework (never modify directly)
│   ├── core/                       # Foundation: BMAD Master, help routing
│   │   ├── agents/
│   │   │   └── sarah-master.md     # Sarah Boone — Master Orchestrator
│   │   └── workflows/
│   ├── bmm/                        # Business Module: Product lifecycle
│   │   ├── agents/                 # PM, Analyst, Architect, Dev, QA, UX
│   │   └── workflows/
│   ├── bmb/                        # Builder Module: Create agents/workflows
│   │   ├── agents/
│   │   └── workflows/
│   ├── cis/                        # Creative Module: Brainstorming, design thinking
│   │   ├── agents/
│   │   └── workflows/
│   ├── tea/                        # Test Module: ATDD, risk-based testing
│   │   ├── agents/
│   │   └── workflows/
│   └── _memory/                    # Memory configuration
│       └── config.yaml
│
├── _bmad-output/                   # All generated artifacts
│   ├── planning-artifacts/         # PRDs, UX designs, architecture docs
│   ├── implementation-artifacts/   # Code and deliverables
│   ├── test-artifacts/             # Test plans, reviews
│   └── bmb-creations/              # New agents, modules, workflows
│
├── .claude/skills/                 # Claude Code skills (auto-loaded)
├── .env                            # Environment variables
└── README.md                       # This file
```

---

## 🚀 Quick Start

### Prerequisites

1. **Claude Code** (or compatible AI coding tool)
2. **Docker** (for Neo4j memory graph)
3. **Node.js** (for MCP servers)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd bmad
```

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
# Neo4j (Memory Graph)
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_secure_password

# Notion (Document Storage)
NOTION_TOKEN=your_notion_integration_token

# Tavily (Web Search)
TAVILY_TOKEN=your_tavily_api_key
```

### 3. Start Neo4j (Memory Graph)

```bash
# Using Docker (recommended)
docker run -d \
  --name neo4j \
  --restart unless-stopped \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/your_secure_password \
  -v neo4j_data:/data \
  neo4j:latest

# Or use Docker Compose
docker-compose up -d neo4j
```

### 4. Start MCP Gateway

```bash
# The MCP gateway provides tool access for agents
docker run -d \
  --name mcp-gateway \
  --restart unless-stopped \
  -p 8811:8811 \
  -e NEO4J_URI=bolt://172.17.0.1:7687 \
  -e NEO4J_USERNAME=neo4j \
  -e NEO4J_PASSWORD=your_secure_password \
  -e NOTION_TOKEN=your_notion_token \
  docker/mcp-gateway
```

### 5. Verify Setup

```bash
# Check Neo4j is running
docker ps | grep neo4j

# Check MCP gateway
curl http://localhost:8811/mcp

# Test memory connection
# (Run from Claude Code: neo4j-memory search query="*")
```

---

## 🎭 Meet the Agents

BMAD operates through specialized AI agents, each with a unique persona and expertise:

| Module | Agent | Role | Trigger Command |
|--------|-------|------|-----------------|
| **Core** | **Sarah Boone** | Master Orchestrator | `/bmad-agent-bmad-master` |
| BMM | Jay | Product Manager | `/bmad-bmm-create-product-brief` |
| BMM | Alan | Systems Analyst | `/bmad-bmm-create-prd` |
| BMM | Fred | Solution Architect | `/bmad-bmm-create-architecture` |
| BMM | Linus | Developer | `/bmad-bmm-dev-story` |
| BMM | Barbara | QA Engineer | `/bmad-bmm-code-review` |
| BMM | Don | UX Designer | `/bmad-bmm-create-ux` |
| BMB | Agent Smith | Agent Builder | `/bmad-bmb-create-agent` |
| CIS | Mike Power | Copywriting | `/bmad-cis-copywriting` |
| TEA | Troy | Test Architect | `/bmad-tea-testarch-framework` |

**Legendary Anchors:** Each agent is inspired by a computing legend and embodies their principles.

---

## ⌨️ Slash Commands

### Entry Points

```
/bmad-agent-bmad-master     # Sarah Boone — unified menu routing
/bmad-help                  # Context-aware help routing
```

### BMM Lifecycle (Business Module)

```
# Planning
/bmad-bmm-create-product-brief    # Create product brief with Jay
/bmad-bmm-create-prd             # Create PRD with Alan
/bmad-bmm-create-architecture    # Design architecture with Fred

# Development
/bmad-bmm-create-epics-and-stories   # Generate epics/stories
/bmad-bmm-create-story               # Create single story
/bmad-bmm-dev-story                  # Develop story with Linus

# Management
/bmad-bmm-sprint-planning        # Sprint planning session
/bmad-bmm-sprint-status          # Check sprint status
/bmad-bmm-code-review            # Code review with Barbara
```

### BMB Builder (Agent/Module Creation)

```
/bmad-bmb-create-agent           # Create new agent
/bmad-bmb-create-workflow        # Create new workflow
/bmad-bmb-create-module          # Create new module
/bmad-bmb-validate-agent         # Validate agent file
/bmad-bmb-validate-workflow      # Validate workflow
```

### CIS Creative (Creative Intelligence)

```
/bmad-cis-brainstorming          # Brainstorming session
/bmad-cis-design-thinking        # Design thinking workshop
/bmad-cis-innovation-strategy     # Innovation strategy
/bmad-cis-copywriting            # Copywriting with Mike Power
```

### TEA Testing (Test Architecture)

```
/bmad-tea-testarch-framework     # Setup test framework
/bmad-tea-testarch-atdd          # ATDD workflow
/bmad-tea-testarch-test-design   # Test design patterns
```

---

## 🧠 Memory System (Neo4j)

BMAD uses Neo4j as its **organizational memory**. Every session, decision, and workflow state is stored and retrieved.

### Memory Types

- **OrchestrationSession** — Workflow sessions and state
- **AGENT_ROUTED** — Agent routing decisions
- **HANDOFF_EXECUTED** — Context handoffs between agents
- **CONFLICT_RESOLVED** — Conflict resolutions
- **DECISION_RECORDED** — Key decisions with rationale
- **BLOCKER_SURFACED** — Blockers and resolutions

### Querying Memory

```cypher
// Search all memories
MATCH (n:Memory) RETURN n LIMIT 10

// Find agent routing history
MATCH (a:AIAgent)-[r:LOGGED]->(e:Event)
WHERE e.event_type = "AGENT_ROUTED"
RETURN a.name, e.description, e.timestamp

// Find recent orchestration sessions
MATCH (s:OrchestrationSession)
RETURN s.goal, s.timestamp, s.active_agents
ORDER BY s.timestamp DESC
```

---

## 🔧 Configuration

### Module Config (`_bmad/bmm/config.yaml`)

```yaml
user_name: "Your Name"
communication_language: "english"
document_output_language: "english professional"
output_folder: "{project-root}/_bmad-output"
```

### Agent Customization

Create `{agent-name}.customize.yaml` in `_bmad/_config/agents/`:

```yaml
name: "jay-custom"
overrides:
  communication_style: "formal"
  decision_heuristics:
    - "Focus on user value first"
```

### MCP Configuration

**For Claude Code** (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "neo4j-memory": {
      "command": "npx",
      "args": ["-y", "@sylweriusz/mcp-neo4j-memory-v2"],
      "env": {
        "NEO4J_URI": "bolt://localhost:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "your_password"
      }
    },
    "neo4j-cypher": {
      "command": "npx",
      "args": ["-y", "neo4j-mcpserver"],
      "env": {
        "NEO4J_URI": "bolt://localhost:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "your_password"
      }
    }
  }
}
```

---

## 🏗️ Creating Custom Agents

### 1. Agent File Structure

```markdown
---
name: "my-agent"
description: "What this agent does"
agent: "Persona Name"
title: "Agent Title"
icon: "🎯"
---

# Core Philosophy

Brief statement of agent's core belief.

## Persona

| Attribute | Value |
|-----------|-------|
| Role | What they do |
| Identity | Who they are |
| Communication Style | How they speak |

## Activation Protocol

1. Load persona
2. Load configuration
3. Retrieve memories
4. [Additional steps...]

## Menu

| Cmd | Description | Handler |
|-----|-------------|---------|
| [AC] | Action A | exec: path/to/action.md |
| [BB] | Action B | workflow: path/to/workflow.yaml |

## Rules

- Rule 1
- Rule 2
```

### 2. Create Using BMB

```bash
/bmad-bmb-create-agent
```

Follow the prompts to generate the agent file.

### 3. Validate

```bash
/bmad-bmb-validate-agent --file _bmad/bmb/agents/my-agent.md
```

---

## 📊 Workflow Architecture

Workflows use a **step-file architecture**:

```
workflows/my-workflow/
├── workflow.yaml          # Workflow definition
├── step-01-init.md        # Step 1: Initialization
├── step-02-process.md     # Step 2: Processing
└── step-03-complete.md    # Step 3: Completion
```

Each step is loaded **just-in-time** and executed in order. State is tracked in frontmatter `stepsCompleted` array.

---

## 🎨 Output Artifacts

All artifacts are saved to `_bmad-output/`:

| Directory | Contents |
|-----------|----------|
| `planning-artifacts/` | PRDs, architecture docs, UX designs |
| `implementation-artifacts/` | Code, scripts, configs |
| `test-artifacts/` | Test plans, reviews, traceability matrices |
| `bmb-creations/` | New agents, modules, workflows |

---

## 🐛 Troubleshooting

### Neo4j Connection Failed

```bash
# Check if Neo4j is running
docker ps | grep neo4j

# If not running, start it
docker start neo4j

# Check logs
docker logs neo4j

# Verify connection
cypher-shell -u neo4j -p your_password
```

### MCP Tools Not Available

```bash
# Check MCP gateway
docker ps | grep mcp-gateway

# Restart if needed
docker restart mcp-gateway

# View logs
docker logs mcp-gateway -f
```

### Agent Not Found

- Ensure agent file exists in correct module (`_bmad/*/agents/`)
- Check file extension is `.md`
- Verify frontmatter has required fields (`name`, `description`)

---

## 📚 Best Practices

1. **Never break character** — Stay in agent persona until exit
2. **Load configs first** — Verify config.yaml loads before proceeding
3. **Execute workflows in order** — No skipping steps
4. **Save after each step** — Never batch multiple steps
5. **Use fuzzy matching** — Menu items match on partial text
6. **Document decisions** — Update story files with implementation notes
7. **Log to memory** — Every significant event should be stored in Neo4j

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-agent`)
3. Commit your changes (`git commit -m 'Add amazing agent'`)
4. Push to the branch (`git push origin feature/amazing-agent`)
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file

---

## 🙏 Acknowledgments

BMAD agents are inspired by computing legends:

- **Sarah Boone** → Clarence Ellis (Groupware, CSCW)
- **Jay** → Jeff Sutherland (Scrum)
- **Alan** → Alan Turing (Computer Science)
- **Fred** → Fred Brooks (Software Engineering)
- **Linus** → Linus Torvalds (Linux)
- **Barbara** → Barbara Liskov (Programming)
- **Don** → Don Norman (UX Design)

---

## 🔗 Links

- [BMAD Documentation](https://github.com/your-org/bmad/docs)
- [Agent Gallery](https://github.com/your-org/bmad/agents)
- [Workflow Library](https://github.com/your-org/bmad/workflows)
- [Issue Tracker](https://github.com/your-org/bmad/issues)

---

> **"Technology should help people work together more effectively, not just work faster individually."**
> — Clarence Ellis (via Sarah Boone)

**🧙 BMAD Master Status:** Ready for orchestration
