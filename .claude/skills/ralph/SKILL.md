---
name: ralph
description: Work with Ralph autonomous development patterns, dual-persistence architecture, and OpenCode integration. Use when executing autonomous dev loops, managing progress.txt state, integrating OpenCode agents, or implementing state machine workflows.
---

# Ralph Autonomous Development Skill

Work with Ralph patterns for autonomous AI-driven development with OpenCode, dual-persistence state management, and state-machine execution.

---

## Quick Start

### What is Ralph?

Ralph is an autonomous AI development loop that runs repeatedly until all PRD items are complete. Each iteration is a fresh instance with clean context, using **dual-persistence architecture**.

### When to Use This Skill

**Use `/ralph` when:**
- Setting up autonomous development workflows with OpenCode
- Implementing `progress.txt` state management
- Executing Ralph's state machine (INIT → MEMORY_LOAD → STORY_SELECT → IMPLEMENT → TEST → VALIDATE → COMMIT/BLOCKER)
- Integrating dual-persistence (operational state + wisdom layer)
- Debugging autonomous dev loops or retry logic
- Designing rollback and checkpoint strategies
- Connecting OpenCode agents to BMAD workflows

---

## Core Concepts

### Dual-Persistence Architecture

| Layer | Purpose | Storage | Read By |
|-------|---------|---------|---------|
| **Operational State** | Current task, what's next | `progress.txt` (YAML) | Ralph (cold start) |
| **Wisdom / Patterns** | What worked, known bugs, code patterns | Neo4j memory graph | Brooks (within iteration) |
| **Audit Trail** | Proof of work, atomic commits | Git history | Both |

**Principle:** No redundancy. Each layer serves a distinct purpose.

### State Machine

```
INIT → MEMORY_LOAD → STORY_SELECT → IMPLEMENT → TEST → VALIDATE → COMMIT
                                             ↓                              ↓
                                          BLOCKER ←←←←←←←←←←←←←←←←←←←←←────┘
```

**States:**
- **INIT**: Load `progress.txt`, validate environment
- **MEMORY_LOAD**: Search Neo4j patterns, fallback to file-only
- **STORY_SELECT**: Pick next task/subtask from queue
- **IMPLEMENT**: Red-green-refactor cycle
- **TEST**: Run verification commands
- **VALIDATE**: Check acceptance criteria
- **COMMIT**: Atomic commit + update `progress.txt`
- **BLOCKER**: Max retries exceeded, log and continue

---

## Commands Reference

### Essential Ralph OpenCode Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `ralph "prompt"` | Execute autonomous loop | `ralph "Implement next story task"` |
| `ralph --status` | Check iteration progress | `ralph --status` |
| `ralph --add-context "hint"` | Inject context | `ralph --add-context "Focus on auth"` |

### OpenCode Agent Selection

| Agent | Use Case | 
|-------|----------|
| `opencode` | Default (GPT-5.2) |
| `codex` | Code generation, refactoring |
| `gemini` | Large context, planning |

---

## Instructions

### Step 1: Initialize Ralph Environment

**Prerequisites:**
- OpenCode CLI installed: `npm install -g @anthropic-ai/opencode`
- `progress.txt` exists in project root
- Ralph prompt template: `ralph_prompt.md`

**Setup:**

```bash
# Clone the project
source ~/.bashrc

# Verify progress.txt exists
cat progress.txt

# Check ralph_prompt.md
ls -la ralph_prompt.md
```

### Step 2: Configure Dual-Persistence

**progress.txt Schema:**

```yaml
---
workflow: ralph-bmad-integration
project: ddpay
iteration: 47
last_updated: 2026-02-16T18:30:00Z

stories:
  - id: story-2-1
    status: complete  # not_started | in_progress | complete | blocked
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
    blocker_reason: "Database timeout"
    blocker_type: transient
    requires_human: true

current_iteration:
  ralph_instance_id: ralph-47
  start_time: 2026-02-16T18:25:00Z
  brooks_context_window_used: 45%

metrics:
  tasks_completed_this_session: 2
  blockers_encountered: 1
```

**Neo4j Event Types (Wisdom Layer):**

| Event Type | Trigger | Key Observations |
|------------|---------|------------------|
| `RALPH_ITERATION_START` | Beginning of spawn | iteration_id, story_id |
| `BROOKS_TASK_ATTEMPT` | Task start | task_id, retry_count |
| `BROOKS_TASK_COMPLETE` | Success | files_modified, tests_passed |
| `BROOKS_TASK_BLOCKER` | Max retries | error, fix_sources_tried |
| `TEST_FAILURE_PATTERN` | Aggregated failures | failure_type, frequency |
| `CODE_PATTERN_REUSE` | Pattern application | pattern_name, reuse_context |

### Step 3: Execute Ralph Loop

**Basic Execution:**

```bash
ralph "Execute the next BMAD story subtask from progress.txt." \
  --agent opencode \
  --prompt-template ralph_prompt.md \
  --max-iterations 50
```

**⚠️ Important:** Do NOT use `--tasks` flag — Ralph's task selection conflicts with BMAD's STORY_SELECT logic in the prompt.

**With Context Injection:**

```bash
ralph "Execute the next BMAD story subtask. Focus on the HeroCarousel component." \
  --agent opencode \
  --prompt-template ralph_prompt.md \
  --max-iterations 30
```

### Step 4: Monitor and Debug

**Check Progress:**

```bash
ralph --status
```

**Read progress.txt:**

```bash
# See current state
cat progress.txt | grep "status:"

# See blockers
cat progress.txt | grep -A 3 "status: blocked"
```

**Add Mid-Loop Context:**

```bash
ralph --add-context "The API timeout was due to Neon cold start. Add retry logic."
```

### Step 5: Handle Blockers

**When Ralph hits a blocker:**

1. **Check progress.txt** for blocker details
2. **For transient blockers** (network, DB timeout):
   - Wait 3 iterations (Ralph auto-retries once)
3. **For permanent blockers** (missing dependency):
   - Edit `progress.txt` to mark `requires_human: true`
   - Resolve the blocker manually
   - Reset `retry_count: 0` and `status: in_progress`

**Unblock Protocol:**

```yaml
# Edit progress.txt
- id: story-2-3
  status: in_progress  # was: blocked
  retry_count: 0       # reset on unblock
  # ... rest of config
```

### Step 6: Recovery Patterns

**If Neo4j is unavailable:**

Ralph continues with file-only context. Check `progress.txt` for:

```yaml
current_iteration:
  neo4j_connected: false
  pending_neo4j_logs: 3
```

Next iteration will attempt backfill if Neo4j recovers.

**If context window exceeds 80%:**

Ralph writes context summary, commits work, and exits cleanly. Next spawn starts fresh.

---

## Guardrails

| Constraint | Rule |
|------------|------|
| **Secrets** | Never print `.env`, tokens, or credentials |
| **Git Safety** | No `reset --hard`, no force push |
| **Scope Control** | Only implement mapped story tasks/subtasks |
| **Test Verification** | Must run tests, don't claim pass without evidence |
| **Retry Limit** | Max 2 retries per task (3 total attempts) |
| **BLOCKER Logging** | Always log blockers to `progress.txt` + Neo4j |

---

## Output Contracts

Ralph terminates with one of these promises:

| Output | Meaning | Next Action |
|--------|---------|-------------|
| `<promise>COMPLETED</promise>` | All stories done | Exit loop |
| `<promise>READY_FOR_NEXT_TASK</promise>` | Subtask done, continue | Spawn next iteration |
| `<promise>BLOCKED</promise>` | Max retries exceeded | Human intervention or skip |
| `<promise>SETUP_REQUIRED</promise>` | Missing files | Fix environment |

---

## Integration with BMAD

### BMAD Agent Chain + Ralph

**Planning Phase:** Jay → James Acosta → Winston → Allura  
**Execution Phase:** Ralph (autonomous loop) → Brooks (within iteration) → Bob → Troy  

**Ralph runs the execution loop**, but delegates to BMAD agents:
- Brooks (via prompt) for implementation
- Bob for story management  
- Troy for test execution

### Workflow Mapping

| BMAD Phase | Ralph Equivalent | Agent |
|------------|------------------|-------|
| Load story context | Read `progress.txt` | Ralph |
| Select next task | STORY_SELECT state | Ralph |
| Red-green-refactor | IMPLEMENT state | Brooks |
| Run tests | TEST state | Brooks |
| Verify ACs | VALIDATE state | Brooks |
| Atomic commit | COMMIT state | Brooks |
| Mark task complete | Update `progress.txt` | Brooks |

---

## Examples

See [examples.md](examples.md) for complete workflows:
- Initial Ralph setup
- Executing a full story
- Handling transient blockers
- Recovery from context exhaustion
- Integration with Neo4j memory

For detailed patterns, see [dual-persistence.md](dual-persistence.md).
For state machine specs, see [state-machine.md](state-machine.md).

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Infinite loops | Missing retry limit | Check `retry_count >= 2` triggers BLOCKER |
| Lost state | No `progress.txt` | Create YAML file, include `status` fields |
| Neo4j timeouts | Connection down | Ralph auto-falls back; check `progress.txt` |
| Context overflow | Too many iterations | Monitor `context_window_used`, exit at 80% |
| Test failures | Missing test runner | Check for vitest/playwright in deps |

---

## References

- [Dual-Persistence Architecture](dual-persistence.md)
- [State Machine Specification](state-machine.md)
- [Practical Examples](examples.md)
- Notion Source: [Architecture — Ralph Integration](https://www.notion.so/Architecture-Ralph-Integration-d345c10a455c478698c0344b2844cbd4)
- OpenCode Docs: https://docs.opencode.ai
