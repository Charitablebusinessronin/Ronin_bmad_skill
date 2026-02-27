---
name: payload-overview
description: Core principles and quick reference for Payload CMS development
---

# Payload CMS Development Rules

You are an expert Payload CMS developer. When working with Payload projects, follow these rules:

## Core Principles

1. **TypeScript-First**: Always use TypeScript with proper types from Payload
2. **Security-Critical**: Follow all security patterns, especially access control
3. **Type Generation**: Run `generate:types` script after schema changes
4. **Transaction Safety**: Always pass `req` to nested operations in hooks
5. **Access Control**: Understand Local API bypasses access control by default

## Project Structure

```
src/
├── app/
│   ├── (frontend)/          # Frontend routes
│   └── (payload)/           # Payload admin routes
├── collections/             # Collection configs
├── globals/                 # Global configs
├── components/              # Custom React components
├── hooks/                   # Hook functions
├── access/                  # Access control functions
└── payload.config.ts        # Main config
```

## Quick Reference

| Task                  | Solution                           |
| --------------------- | ---------------------------------- |
| Auto-generate slugs   | `slugField()`                      |
| Restrict by user      | Access control with query          |
| Local API user ops    | `user` + `overrideAccess: false`   |
| Draft/publish         | `versions: { drafts: true }`       |
| Computed fields       | `virtual: true` with afterRead     |
| Conditional fields    | `admin.condition`                  |
| Custom validation     | `validate` function                |
| Filter relationships  | `filterOptions` on field           |

## Resources

- Docs: https://payloadcms.com/docs
- LLM Context: https://payloadcms.com/llms-full.txt
- GitHub: https://github.com/payloadcms/payload
