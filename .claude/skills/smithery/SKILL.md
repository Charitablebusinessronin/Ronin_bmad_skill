---
name: smithery
description: Use Smithery MCP to connect to Notion, search, fetch pages, and manage connections. Also use smithery CLI for namespace and skill management.
homepage: https://smithery.ai
---

# Smithery Skill

Use Smithery to connect to MCP servers like Notion, manage your namespace, and install skills.

## Quick Reference

### MCP Connections
- **Add server**: `smithery mcp add <server-slug>`
- **List tools**: `smithery tool list <connection>`
- **Call tool**: `smithery tool call <connection> <tool> '{"key": "value"}'`
- **List connections**: `smithery mcp list`

### Namespace Management
- **Your namespace**: `roninsmith` (stored in `.env.local` as `SMITHERY_NAMESPACE`)

### Skills
- **Install skill**: `smithery skill add <namespace>/<skill-slug>`
- **Upvote**: `smithery skill upvote <namespace>/<slug>`
- **Downvote**: `smithery skill downvote <namespace>/<slug>`
- **Review**: `smithery skill review add <namespace>/<slug> --review "..." --vote up`

## Environment Variables

Required in `.env.local`:
```
SMITHERY_NAMESPACE=roninsmith
NOTION_TOKEN=your_notion_token
```

## Common Tools

### Notion (via smithery)
- `smithery tool call notion notion-search '{"query": "search term"}'`
- `smithery tool call notion notion-fetch '{"id": "page-id"}'`
- `smithery tool call notion notion-create-pages '{"pages": [...]}`
- `smithery tool call notion notion-update-page '{"page_id": "...", "command": "update_properties", "properties": {...}}'`

### Smithery MCP Commands
- `smithery mcp add notion` - Add Notion MCP
- `smithery mcp list` - List all MCP connections
- `smithery mcp remove <connection>` - Remove connection

## Usage Notes

1. **Authorization**: If Notion requires auth, run: `open "https://api.smithery.ai/connect/roninsmith/notion/auth"`
2. **Namespace**: Always use `roninsmith` for your personal skills
3. **Tools**: Use the smithery CLI commands directly via bash tool

## Example Workflows

**Search Notion for Gilliam:**
```bash
smithery tool call notion notion-search '{"query": "Gilliam BMAD Master"}'
```

**Fetch a page:**
```bash
smithery tool call notion notion-fetch '{"id": "page-id-here"}'
```

**Add a new MCP server:**
```bash
smithery mcp add <server-name>
```

---

**Last Updated**: 2026-03-03
**Namespace**: roninsmith
