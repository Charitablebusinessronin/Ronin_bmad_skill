---
name: fields
description: Field types, patterns, and configurations
---

# Payload CMS Fields

## Common Field Patterns

```typescript
// Auto-generate slugs
import { slugField } from 'payload'
slugField({ fieldToUse: 'title' })

// Relationship with filtering
{
  name: 'category',
  type: 'relationship',
  relationTo: 'categories',
  filterOptions: { active: { equals: true } },
}

// Conditional field
{
  name: 'featuredImage',
  type: 'upload',
  relationTo: 'media',
  admin: {
    condition: (data) => data.featured === true,
  },
}

// Virtual field
{
  name: 'fullName',
  type: 'text',
  virtual: true,
  hooks: {
    afterRead: [({ siblingData }) => `${siblingData.firstName} ${siblingData.lastName}`],
  },
}
```

## Field Types

### Text Field
```typescript
{
  name: 'title',
  type: 'text',
  required: true,
  unique: true,
  minLength: 5,
  maxLength: 100,
  index: true,
}
```

### Relationship
```typescript
// Single relationship
{
  name: 'author',
  type: 'relationship',
  relationTo: 'users',
  required: true,
  maxDepth: 2,
}

// Multiple relationships
{
  name: 'categories',
  type: 'relationship',
  relationTo: 'categories',
  hasMany: true,
}
```

### Upload
```typescript
{
  name: 'featuredImage',
  type: 'upload',
  relationTo: 'media',
  required: true,
}
```

## Validation

```typescript
{
  name: 'email',
  type: 'email',
  validate: (value, { operation }) => {
    if (operation === 'create' && !value) {
      return 'Email is required'
    }
    return true
  },
}
```
