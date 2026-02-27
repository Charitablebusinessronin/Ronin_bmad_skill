# progress.txt Specification

The **progress.txt** file is the operational truth for Ralph-BMAD integration. It serves as the source of truth for workflow state, task progress, and retry tracking across iterations.

## Schema (YAML)

```yaml
---
workflow: ralph-bmad-integration
project: ddpay
iteration: 47
last_updated: 2026-02-16T18:30:00Z

stories:
  - id: story-2-1
    status: complete
    tasks_completed: 8
    tasks_total: 8
    last_commit: a1b2c3d
    
  - id: story-2-2
    status: in_progress
    current_task: task-3
    retry_count: 1
    last_action: implement
    
  - id: story-2-3
    status: blocked
    blocker_reason: "Database connection timeout during seed"
    blocker_type: transient  # transient | permanent
    blocker_logged_to_neo4j: true
    neo4j_event_id: d=xyz123
    requires_human: true

current_iteration:
  ralph_instance_id: ralph-47
  start_time: 2026-02-16T18:25:00Z
  brooks_context_window_used: 45%
  
metrics:
  tasks_completed_this_session: 2
  blockers_encountered: 1
  avg_iteration_time_ms: 125000
```

## Field Definitions

### Header Fields

| Field | Type | Description |
|-------|------|-------------|
| `workflow` | string | Identifies the workflow type (ralph-bmad-integration) |
| `project` | string | Project identifier |
| `iteration` | number | Current iteration count |
| `last_updated` | ISO 8601 datetime | Last modification timestamp |

### Story Entry Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✓ | Story identifier (e.g., story-2-1) |
| `status` | enum | ✓ | `not_started`, `in_progress`, `blocked`, `complete` |
| `tasks_completed` | number | For complete stories | Total completed tasks |
| `tasks_total` | number | For complete stories | Total tasks in story |
| `last_commit` | string | For complete stories | Git commit hash |
| `current_task` | string | For in_progress stories | Active task ID |
| `retry_count` | number | For in_progress stories | Current retry attempt (0-indexed) |
| `last_action` | string | For in_progress stories | Last executed state |
| `blocker_reason` | string | For blocked stories | Description of blocker |
| `blocker_type` | enum | For blocked stories | `transient` or `permanent` |
| `blocker_logged_to_neo4j` | boolean | For blocked stories | Whether event was logged |
| `neo4j_event_id` | string | Optional | Neo4j event reference |
| `requires_human` | boolean | For blocked stories | Whether human intervention needed |

### Current Iteration Fields

| Field | Type | Description |
|-------|------|-------------|
| `ralph_instance_id` | string | Unique iteration identifier |
| `start_time` | ISO 8601 datetime | When iteration began |
| `brooks_context_window_used` | percentage | Context budget consumed |

### Metrics Fields

| Field | Type | Description |
|-------|------|-------------|
| `tasks_completed_this_session` | number | Tasks done in current session |
| `blockers_encountered` | number | Total blockers hit |
| `avg_iteration_time_ms` | number | Average iteration duration |

## Status Transitions

```
not_started → in_progress (task selected)
in_progress → complete (all tasks done)
in_progress → blocked (max retries exceeded)
blocked → in_progress (human unblocks)
blocked → complete (if auto-resolved)
```

## Retry Logic

- **Retry count** increments on each failure
- **Reset to 0** on successful completion
- **Blocker triggered** when `retry_count >= 3` (3 total attempts)
- **Human unblock** resets retry count to 0

## Blocking Strategy

```yaml
# Blocker entry on retry_count >= 2
status: blocked
blocker_reason: "Specific description of failure"
blocker_type: transient  # May auto-retry after delay
requires_human: true      # User must edit progress.txt
blocker_logged_to_neo4j: true
neo4j_event_id: "d=xyz123"
```

Human unblocks by:
1. Fixing underlying issue
2. Setting `status: in_progress`
3. Resetting `retry_count: 0`
4. Updating `last_updated` timestamp

## Best Practices

**Atomic Updates**
- Update progress.txt atomically with git commits
- Commit message: `progress: story-X-Y task-N status`

**Validation**
- YAML must parse successfully
- All `in_progress` stories need `current_task`
- All `blocked` stories need `blocker_reason`

**Backup**
- Git tracks all progress.txt changes
- History provides audit trail of workflow execution
