---
name: mcp-integrations
description: Configure and use MCP tools in Cursor and OpenCode across common integrations (Neo4j memory graph, Notion, Context7). Use when wiring MCP servers in mcp.json/opencode.json, troubleshooting MCP auth/connectivity, or prompting agents to use specific MCP tool prefixes (e.g., neo4j-cypher_*, notion_*, context7_*).
---

# MCP Integrations

Guide for using MCP (Model Context Protocol) servers in Cursor IDE and OpenCode CLI.

## Quick Reference

| MCP Server | Cursor | OpenCode | Tool Prefix | Use For |
|------------|--------|----------|-------------|---------|
| **neo4j-cypher** | ✅ | ✅ | `neo4j-cypher_*` | Cypher queries, graph analysis |
| **neo4j-memory** | ✅ | ✅ | `neo4j-memory_*` | Semantic memory, project knowledge |
| **notion** | ✅ | ✅ | `notion_*` | Pages, databases, workspaces |
| **context7** | ✅ | ✅ | `context7_*` | Documentation search, API lookup |

## MCP Server Configuration

### Cursor (mcp.json)

```json
{
  "mcpServers": {
    "neo4j-cypher": {
      "command": "npx",
      "args": ["-y", "neo4j-mcpserver"],
      "env": {
        "NEO4J_URI": "bolt://host.docker.internal:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "your-password"
      }
    },
    "neo4j-memory": {
      "command": "npx",
      "args": ["-y", "@sylweriusz/mcp-neo4j-memory-v2"],
      "env": {
        "NEO4J_URI": "bolt://host.docker.internal:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "your-password"
      }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--api-key", "your-api-key"]
    },
    "notion": {
      "url": "https://mcp.notion.com/mcp",
      "headers": {
        "Authorization": "Bearer your-token"
      }
    }
  }
}
```

### OpenCode (opencode.json)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "neo4j-cypher": {
      "type": "local",
      "command": ["npx", "-y", "neo4j-mcpserver"],
      "enabled": true,
      "environment": {
        "NEO4J_URI": "bolt://host.docker.internal:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "your-password"
      }
    },
    "neo4j-memory": {
      "type": "local",
      "command": ["npx", "-y", "@sylweriusz/mcp-neo4j-memory-v2"],
      "enabled": true,
      "environment": {
        "NEO4J_URI": "bolt://host.docker.internal:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "your-password"
      }
    },
    "context7": {
      "type": "local",
      "command": ["npx", "-y", "@upstash/context7-mcp", "--api-key", "your-api-key"],
      "enabled": true
    },
    "notion-mcp-server": {
      "type": "local",
      "command": ["npx", "-y", "@notionhq/notion-mcp-server"],
      "enabled": true,
      "environment": {
        "NOTION_TOKEN": "your-token"
      }
    }
  },
  "tools": {
    "neo4j-cypher_*": true,
    "neo4j-memory_*": true,
    "context7_*": true,
    "notion-mcp-server_*": true
  }
}
```

## Using MCP Tools

### Neo4j Cypher

Query graph database:
```
MATCH (n:Memory) RETURN n.name, n.type LIMIT 10
```

### Neo4j Memory

Search project knowledge:
```
query: "payload cms authentication"
```

### Notion

Fetch page content:
```
page_id: "your-page-id"
```

Query database:
```
database_id: "your-database-id"
filter: {"property": "Status", "select": {"equals": "Active"}}
```

### Context7

Search documentation:
```
query: "Next.js app router"
```

## Troubleshooting

### Connection Issues

1. Verify Neo4j is running: `docker ps | grep neo4j`
2. Check credentials match in both configs
3. Test direct connection: `cypher-shell -u neo4j -p password`

### Auth Errors

- Notion: Token must start with `secret_` or `ntn_`
- Context7: Get API key from https://context7.com
- Neo4j: Default password must be changed on first login

### Tool Not Found

If the server is named `mcp_docker`, tools will look like `mcp_docker_*`.
If the server is named `neo4j-cypher`, tools will look like `neo4j-cypher_*`.

Check the exact server name in your config.

## Reference

- Neo4j Cypher: See [references/neo4j-cypher.md](references/neo4j-cypher.md)
- Notion API: See [references/notion-api.md](references/notion-api.md)
- Context7: See [references/context7.md](references/context7.md)