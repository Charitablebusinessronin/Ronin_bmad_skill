---
name: field-type-guards
description: Runtime field type checking and safe type narrowing
---

# Payload Field Type Guards

Type guards for runtime field type checking and safe type narrowing.

## Most Common Guards

### fieldAffectsData

**Most commonly used guard.** Checks if field stores data (has name and is not UI-only).

```typescript
import { fieldAffectsData } from 'payload'

function generateSchema(fields: Field[]) {
  fields.forEach((field) => {
    if (fieldAffectsData(field)) {
      // Safe to access field.name
      schema[field.name] = getFieldType(field)
    }
  })
}
```

### fieldHasSubFields

Checks if field contains nested fields (group, array, row, or collapsible).

```typescript
import { fieldHasSubFields } from 'payload'

function traverseFields(fields: Field[]): void {
  fields.forEach((field) => {
    if (fieldHasSubFields(field)) {
      // Safe to access field.fields
      traverseFields(field.fields)
    }
  })
}
```

### fieldIsArrayType

Checks if field type is `'array'`.

```typescript
import { fieldIsArrayType } from 'payload'

if (fieldIsArrayType(field)) {
  // field.type === 'array'
  console.log(`Min rows: ${field.minRows}`)
}
```

## Common Patterns

### Recursive Field Traversal

```typescript
import { fieldAffectsData, fieldHasSubFields } from 'payload'

function traverseFields(fields: Field[], callback: (field: Field) => void) {
  fields.forEach((field) => {
    if (fieldAffectsData(field)) {
      callback(field)
    }

    if (fieldHasSubFields(field)) {
      traverseFields(field.fields, callback)
    }
  })
}
```

### Safe Property Access

```typescript
import { fieldSupportsMany } from 'payload'

if (fieldSupportsMany(field) && field.hasMany) {
  console.log('Multiple values supported')
}
```

## All Available Guards

| Type Guard | Checks For | Use When |
| -----------| -----------| ---------|
| `fieldAffectsData` | Field stores data | Need to access field.name |
| `fieldHasSubFields` | Nested fields exist | Recursively traverse fields |
| `fieldIsArrayType` | Field is array type | Distinguish arrays |
| `fieldSupportsMany` | Multiple values supported | Check hasMany support |
| `fieldIsVirtual` | Field is virtual | Skip in database transforms |
