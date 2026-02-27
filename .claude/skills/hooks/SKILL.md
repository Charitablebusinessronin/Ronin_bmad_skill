---
name: hooks
description: Collection hooks, field hooks, and context patterns
---

# Payload CMS Hooks

## Collection Hooks

```typescript
export const Posts: CollectionConfig = {
  slug: 'posts',
  hooks: {
    // Before validation - format data
    beforeValidate: [
      async ({ data, operation }) => {
        if (operation === 'create') {
          data.slug = slugify(data.title)
        }
        return data
      },
    ],

    // Before save - business logic
    beforeChange: [
      async ({ data, req, operation, originalDoc }) => {
        if (operation === 'update' && data.status === 'published') {
          data.publishedAt = new Date()
        }
        return data
      },
    ],

    // After save - side effects
    afterChange: [
      async ({ doc, req, operation, previousDoc, context }) => {
        if (context.skipNotification) return

        if (operation === 'create') {
          await sendNotification(doc)
        }
        return doc
      },
    ],

    // Before delete - cascading deletes
    beforeDelete: [
      async ({ req, id }) => {
        await req.payload.delete({
          collection: 'comments',
          where: { post: { equals: id } },
          req,
        })
      },
    ],
  },
}
```

## Hook Context

Share data between hooks or control hook behavior using request context:

```typescript
export const Posts: CollectionConfig = {
  slug: 'posts',
  hooks: {
    beforeChange: [
      async ({ context }) => {
        context.expensiveData = await fetchExpensiveData()
      },
    ],
    afterChange: [
      async ({ context, doc }) => {
        await processData(doc, context.expensiveData)
      },
    ],
  },
}
```

## Best Practices

- Use `beforeValidate` for data formatting
- Use `beforeChange` for business logic
- Use `afterChange` for side effects
- Use `afterRead` for computed fields
- Store expensive operations in `context`
- Pass `req` to nested operations for transaction safety
- Use context flags to prevent infinite loops
