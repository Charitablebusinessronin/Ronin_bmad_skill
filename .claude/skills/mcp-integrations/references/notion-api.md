# Notion MCP Reference

## Authentication

### Integration Token
1. Go to https://www.notion.so/my-integrations
2. Create new integration
3. Copy token (starts with `secret_`)
4. Share pages/databases with integration

### Token Format
```json
{
  "NOTION_TOKEN": "secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

## Common Operations

### Fetch Page
```
page_id: "page-uuid-here"
```

### Query Database
```json
{
  "database_id": "db-uuid-here",
  "filter": {
    "property": "Status",
    "select": {
      "equals": "In Progress"
    }
  }
}
```

### Create Page
```json
{
  "parent": {"database_id": "db-uuid-here"},
  "properties": {
    "Name": {
      "title": [{"text": {"content": "New Page"}}]
    },
    "Status": {
      "select": {"name": "To Do"}
    }
  }
}
```

### Update Page
```json
{
  "page_id": "page-uuid-here",
  "properties": {
    "Status": {
      "select": {"name": "Done"}
    }
  }
}
```

### Search
```
query: "project requirements"
```

## Database Schema

Common property types:
- `title` - Page title
- `rich_text` - Text content
- `select` - Single select
- `multi_select` - Multiple select
- `status` - Status (Notion native)
- `date` - Date/datetime
- `people` - Person reference
- `relation` - Relation to other DB
- `formula` - Computed value

## Page URL to ID

Convert URL to page ID:
```
https://www.notion.so/Page-Title-1a2b3c4d5e6f7g8h9i0j1k2l
                              └──────┬──────┘
                              Page ID: 1a2b3c4d5e6f7g8h9i0j1k2l
```

Remove dashes for API: `1a2b3c4d-5e6f-7g8h-9i0j-1k2l`