---
name: mcp-servers-reference
description: Reference guide for all MCP servers available in the ddpay project. Use when the user asks about MCP servers, needs to configure tools, or wants to understand what capabilities are available. Covers Docker MCP Gateway, Notion, Neo4j, Context7, and zero-config servers.
---

# MCP Servers Reference

Complete catalog of MCP servers configured and available for the ddpay project.

---

## 🔥 Currently Enabled

### MCP_DOCKER (Docker MCP Gateway)
**Type:** Local (WSL)  
**Status:** ✅ ENABLED  
**Command:** `wsl.exe docker.exe mcp gateway run`

**Environment:**
```json
{
  "DOCKER_HOST": "npipe:////./pipe/docker_engine",
  "LOCALAPPDATA": "C:\\Users\\SabirAsheed\\AppData\\Local",
  "ProgramData": "C:\\ProgramData",
  "ProgramFiles": "C:\\Program Files"
}
```

**Capabilities:**
- `mcp_docker_get_neo4j_schema(sample_size)` - Get Neo4j schema
- `mcp_docker_search_memories(query)` - Search project memories
- `mcp_docker_read_neo4j_cypher(query)` - Execute Cypher queries
- `mcp_docker_read_graph()` - Read graph (currently has validation errors with null types)

**Working Functions:**
- ✅ Schema retrieval
- ✅ Memory search (returns entities + relations)
- ✅ Cypher queries (MATCH, CREATE, etc.)
- ❌ read_graph() - fails with Pydantic validation on null types/observations

**Issue:** Some Neo4j nodes have `type=null` or `observations=null`, causing read_graph() to fail.

---

## 🔧 Configured but Disabled

### Neo4j-Cypher (Standalone)
**Type:** Local  
**Status:** ❌ DISABLED (schema validation error)  
**Command:** `npx -y neo4j-mcpserver`

**Environment:**
```json
{
  "NEO4J_URI": "bolt://host.docker.internal:7687",
  "NEO4J_USER": "neo4j",
  "NEO4J_PASSWORD": "Kamina2025*"
}
```

**Issue:** `Invalid schema for function 'neo4j-cypher-update-pulse'` - missing items in array schema.

---

### Neo4j-Memory
**Type:** Local  
**Status:** ❌ DISABLED  
**Command:** `npx -y @sylweriusz/mcp-neo4j-memory-v2`

**Environment:** Same as Neo4j-Cypher

**Purpose:** Store/retrieve project memories in Neo4j graph.

---

### Context7
**Type:** Local  
**Status:** ❌ DISABLED  
**Command:** `npx -y @upstash/context7-mcp --api-key [KEY]`

**API Key:** `ctx7sk-ec35abd7-3618-43ea-900b-28c0e3946685`

**Purpose:** Search documentation with Context7 AI - up-to-date library docs, API references.

**Usage:** Ask "How does X work?" → searches Context7 automatically.

---

### Notion-MCP-Server (Local)
**Type:** Local  
**Status:** ❌ DISABLED  
**Command:** `npx -y @notionhq/notion-mcp-server`

**Environment:**
```json
{
  "NOTION_TOKEN": "ntn_U79481010438AooMDIvYCPhHWcpqpn9DGJDXTTNVV3udES"
}
```

**Purpose:** Direct local Notion operations (read/write pages, query databases).

---

### Notion (Remote)
**Type:** Remote  
**Status:** ❌ DISABLED  
**URL:** `https://mcp.notion.com/mcp`

**Purpose:** Official Notion-hosted MCP endpoint - OAuth-based authentication.

---

## 🆕 Recommended Zero-Config MCP Servers

### Filesystem
**Purpose:** Read/write local files  
**Config:** Just set allowed paths  
**Command:** `npx -y @modelcontextprotocol/server-filesystem`

**Recommended Args:** `["/home/ronin/Dev/ddpay", "/home/ronin/Dev"]`

---

### Fetch
**Purpose:** Web requests (HTTP GET/POST)  
**Config:** None  
**Command:** `uvx mcp-server-fetch` or `npx -y mcp-server-fetch`

---

### Puppeteer
**Purpose:** Browser automation, screenshots  
**Config:** None  
**Command:** `npx -y @modelcontextprotocol/server-puppeteer`

**Use Case:** Visual testing alongside Playwright.

---

### SQLite
**Purpose:** Local SQLite database  
**Config:** None (creates file automatically)  
**Command:** `npx -y @modelcontextprotocol/server-sqlite`

---

### Time
**Purpose:** Date/time operations  
**Config:** None  
**Command:** `npx -y @modelcontextprotocol/server-time`

---

### Sequential Thinking
**Purpose:** Multi-step reasoning helper  
**Config:** None  
**Command:** `npx -y @modelcontextprotocol/server-sequentialthinking`

---

## 📋 Configuration Files

### Current OpenCode Config
**Location:** `.opencode/opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "mcp_docker": {
      "type": "local",
      "command": ["wsl.exe", "docker.exe", "mcp", "gateway", "run"],
      "enabled": true,
      "environment": { ... }
    }
  }
}
```

### Cursor Config (For Reference)
**Location:** `.cursor/mcp.json`

Contains neo4j-cypher, neo4j-memory, context7, notion-mcp-server, mcp_docker, notion.

---

## 🔧 Troubleshooting

### Neo4j Schema Errors
**Problem:** `read_graph()` fails with Pydantic validation errors.
**Cause:** Nodes with `type=null` or `observations=null`.
**Fix Options:**
1. Clean nodes: `MATCH (n) WHERE n.type IS NULL SET n.type = 'unknown'`
2. Use Cypher queries instead: `mcp_docker_read_neo4j_cypher()`

### Schema Validation Errors
**Problem:** `Invalid schema for function 'X'`.
**Cause:** MCP server sends incomplete JSON schema.
**Fix:** Disable problematic server, use alternative (e.g., mcp_docker for Neo4j).

### Authentication
- **Neo4j:** Connection via `bolt://host.docker.internal:7687`
- **Notion Local:** Token-based (`ntn_U79481010438...`)
- **Notion Remote:** OAuth via browser

---

## 📊 Status Summary

| Server | Type | Status | Issues |
|--------|------|--------|--------|
| mcp_docker | Local | ✅ Working | read_graph has null type errors |
| neo4j-cypher | Local | ❌ Disabled | Schema validation error |
| neo4j-memory | Local | ❌ Disabled | Same Neo4j instance as cypher |
| context7 | Local | ❌ Disabled | Needs API key |
| notion-mcp-server | Local | ❌ Disabled | Token configured |
| notion | Remote | ❌ Disabled | OAuth available |

---

## ✅ Working Commands

Via mcp_docker:
```javascript
// Get Neo4j schema
mcp_docker_get_neo4j_schema(sample_size=100)

// Search memories
mcp_docker_search_memories("agent")

// Run Cypher query
mcp_docker_read_neo4j_cypher("MATCH (n) RETURN count(n)")
```

---

## 📁 Files

- OpenCode: `.opencode/opencode.json`
- Cursor: `.cursor/mcp.json`
- This Skill: `.cursor/skills/mcp-servers-reference/SKILL.md`
