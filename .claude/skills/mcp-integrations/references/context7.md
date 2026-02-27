# Context7 MCP Reference

## Overview

Context7 provides up-to-date documentation search for:
- React, Next.js, Vue, Angular
- Node.js, Python, Go
- Docker, Kubernetes
- AWS, GCP, Azure
- And 1000+ more libraries

## Authentication

### Free Tier
- 50 requests/day
- No API key required

### Pro Tier
- Get API key from https://context7.com
- Higher rate limits

## Usage

### Search Documentation
```
library: "next.js"
query: "app router dynamic routes"
```

### Get Library Info
```
library: "payload"
```

### Code Examples
```
library: "react"
query: "useEffect cleanup function"
includeCode: true
```

## Best Practices

1. **Be specific**: "Next.js 14 app router middleware" vs "next.js"
2. **Include version**: "React 18 concurrent features"
3. **Ask for code**: Add "include code examples" to get snippets
4. **Verify freshness**: Check last updated timestamp

## Response Format

```json
{
  "results": [
    {
      "title": "App Router",
      "content": "...",
      "url": "https://nextjs.org/docs/app",
      "lastUpdated": "2024-01-15"
    }
  ]
}
```

## Troubleshooting

### Rate Limit Hit
```
Error: Rate limit exceeded (50/day on free tier)
Solution: Upgrade at https://context7.com or wait 24h
```

### Library Not Found
```
Error: Library "xyz" not found
Solution: Check spelling, use official npm package name
```

## Alternative: Direct MCP

If Context7 MCP has issues, use direct API:
```bash
curl https://mcp.context7.com/mcp \
  -H "Content-Type: application/json" \
  -d '{"query": "next.js middleware"}'
```