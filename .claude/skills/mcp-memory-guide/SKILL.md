---
name: mcp-memory-guide
description: Guide for using Neo4j memory graph and Notion MCP tools in Cursor. Use when pulling project memories, searching knowledge, or querying Notion databases via MCP tools like neo4j-memory_*, neo4j-cypher_*, and notion_*.
---

# MCP Memory & Notion Guide

How to use Neo4j memories and Notion MCP tools in Cursor.

## Quick Start

### Available MCP Tools

| Tool | Prefix | Use For |
|------|--------|---------|
| Neo4j Memory | `neo4j-memory_*` | Search project memories |
| Neo4j Cypher | `neo4j-cypher_*` | Graph queries |
| Notion | `notion_*` | Pages, databases |

## Neo4j Memory

### Search Project Memories
```
query: "ddpay project setup"
```

### Create Memory
```
name: "MCP Configuration"
content: "Configured neo4j-memory, notion-mcp-server"
type: "milestone"
```

### Retrieve Specific Memory
```
id: "memory-id-here"
```

## Notion MCP

### Fetch Page
```
page_id: "page-uuid-here"
```

### Query Database
```
database_id: "db-uuid-here"
filter: {"property": "Status", "select": {"equals": "Active"}}
```

### Create Page
```
parent: {"database_id": "db-uuid-here"}
properties: {
  "Name": {"title": [{"text": {"content": "New Item"}}]},
  "Status": {"select": {"name": "To Do"}}
}
```

## Workflows

### Pull Context Before Tasks
**Before starting work, always:**
1. Search Neo4j memories for relevant context
2. Check Notion for requirements/docs
3. Use findings to inform your approach

### Save Context After Tasks
**After completing work:**
1. Create/update memory in Neo4j
2. Sync important info to Notion
3. Link related memories and pages

## Examples

**Search for BMAD info:**
```
Search Neo4j for: "BMAD agent structure"
```

**Get Notion requirements:**
```
Fetch Notion page: "2a11d9be65b380fd9f45fc483ff6f2eb"
```

**Save session context:**
```
Create memory: "Session 2026-02-14 - Configured MCP servers"
```

## Configuration

Neo4j connection:
```
URI: bolt://host.docker.internal:7687
User: neo4j
Password: Kamina2025*
```

Notion token: `ntn_U79481010438AooMDIvYCPhHWcpqpn9DGJDXTTNVV3udES`

## Troubleshooting

**No results?**
- Check MCP server is enabled in Cursor settings
- Verify Neo4j is running: `docker ps | grep neo4j`
- Check Notion token is valid

**Connection errors?**
- Ensure Docker Desktop is running
- Verify network access to Neo4j (port 7687)
- Check MCP config in Cursor settings

## Resources

- Neo4j Browser: http://localhost:7474
- Notion API docs: https://developers.notion.com
- Cursor MCP docs: https://docs.cursor.com