---
name: endpoints
description: Custom REST API endpoints with authentication and helpers
---

# Payload Custom Endpoints

## Basic Endpoint Pattern

Custom endpoints are **not authenticated by default**. Always check `req.user`.

```typescript
import { APIError } from 'payload'
import type { Endpoint } from 'payload'

export const protectedEndpoint: Endpoint = {
  path: '/protected',
  method: 'get',
  handler: async (req) => {
    if (!req.user) {
      throw new APIError('Unauthorized', 401)
    }

    const data = await req.payload.find({
      collection: 'posts',
      where: { author: { equals: req.user.id } },
    })

    return Response.json(data)
  },
}
```

## Route Parameters

```typescript
export const trackingEndpoint: Endpoint = {
  path: '/:id/tracking',
  method: 'get',
  handler: async (req) => {
    const { id } = req.routeParams
    const tracking = await getTrackingInfo(id)
    return Response.json(tracking)
  },
}
```

## Error Handling

```typescript
import { APIError } from 'payload'

export const validateEndpoint: Endpoint = {
  path: '/validate',
  method: 'post',
  handler: async (req) => {
    const data = await req.json()

    if (!data.email) {
      throw new APIError('Email is required', 400)
    }

    return Response.json({ valid: true })
  },
}
```

## Best Practices

1. **Always check authentication** - Custom endpoints are not authenticated by default
2. **Use `req.payload` for operations** - Ensures access control and hooks execute
3. **Throw `APIError` for errors** - Provides consistent error responses
4. **Return Web API `Response`** - Use `Response.json()` for consistent responses
