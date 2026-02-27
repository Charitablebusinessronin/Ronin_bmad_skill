# Neo4j Cypher MCP Reference

## Connection Setup

### Docker (Recommended)
```bash
docker run -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:latest
```

### Environment Variables
```
NEO4J_URI=bolt://host.docker.internal:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-secure-password
```

## Common Queries

### List All Nodes
```cypher
MATCH (n) RETURN labels(n), count(n)
```

### Find by Label
```cypher
MATCH (n:Memory) RETURN n LIMIT 10
```

### Search by Property
```cypher
MATCH (n) WHERE n.name CONTAINS "payload" RETURN n
```

### Create Node
```cypher
CREATE (m:Memory {name: "Test", type: "note", created: datetime()})
```

### Create Relationship
```cypher
MATCH (a:Memory {name: "A"}), (b:Memory {name: "B"})
CREATE (a)-[:RELATES_TO]->(b)
```

### Update Node
```cypher
MATCH (n:Memory {name: "Test"})
SET n.updated = datetime()
RETURN n
```

### Delete Node
```cypher
MATCH (n:Memory {name: "Test"})
DELETE n
```

## Data Types

- `datetime()` - Current timestamp
- `date()` - Current date
- `point({latitude: x, longitude: y})` - Geospatial
- Lists: `["item1", "item2"]`
- Maps: `{key: "value"}`

## Best Practices

1. Always use parameters in production
2. Index frequently queried properties
3. Use constraints for uniqueness
4. Profile queries with `EXPLAIN`