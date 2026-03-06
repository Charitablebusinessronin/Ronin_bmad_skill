---
name: ralph-v5
description: Ralph BMAD Agent V5 - Improved version with boundary crossing, CMS verification, and truth-in-reporting
---

# Ralph V5 Workflow

**Goal:** Execute BMAD story implementation with verified user-visible outcomes, not just test-passing

**Version:** 5.0.0
**Based on:** Ralph V3 learnings from Sprint 2 failure (50 iterations, 0 visible stories)
**Date:** 2026-02-19

---

## Problem Statement

**V3 Failure:**

- Claimed 33 stories complete
- 609 tests passing
- But website showed template content

**Root Cause:**

- Ralph optimized for "tests pass" instead of "user sees value"
- No boundary crossing verification
- CMS content population was optional
- No truth-in-reporting

**V5 Solution:**

- Boundary crossing verification at every layer
- CMS state verification mandatory
- Truth-in-reporting with separate metrics
- Progressive documentation

---

## V5 Core Principles

### Principle 1: Verify at Every Boundary

```
Code → Database → API → UI
  ↑         ↑        ↑
Boundary Crossing Verification Required
```

### Principle 2: Truth-in-Reporting

```
OLD: stories_complete: 33
NEW:
  components_built: 33
  cms_populated: 0
  user_visible: 0
```

### Principle 3: Verification is Not Optional

```
A task is NOT complete until its verification passes.
"Implement AND verify" - not "implement OR verify"
```

### Principle 4: Fail Fast, Don't Auto-Populate

```
If CMS content missing → FAIL and report
Don't try to automate content population
Let humans populate, let Ralph verify
```

---

## V5 State Machine

```
INIT → MEMORY_LOAD → STORY_SELECT → IMPLEMENT → TEST → VALIDATE → COMMIT
                                                            ↓
                                              BOUNDARY_VERIFICATION
                                                    ↓
                                          CODE_BOUNDARY → DB_BOUNDARY → API_BOUNDARY → UI_BOUNDARY
                                                    ↓
                                              VERIFICATION_RESULTS
                                                    ↓
                                              [PASS: Continue] [FAIL: Report + Block]
```

---

## Workflow Steps

### Step 01: INIT (Cold Start Fixed)

**Purpose:** Verify environment and select first story

**Actions:**

1. **Verify worktree:**

   ```bash
   pwd | grep ddpay-sprint || echo "ERROR: Wrong directory"
   ```

2. **Verify Docker:**

   ```bash
   docker-compose ps | grep ddpay
   # If not running: docker-compose up -d
   ```

3. **Verify images available:**

   ```bash
   ls public/images/ | wc -l  # Expect 65+
   ```

4. **Read progress.txt:**

   ```bash
   cat progress.txt
   # If missing: output <promise>SETUP_REQUIRED</promise>
   ```

5. **Story selection (cold-start fixed):**
   - Look for `status: in_progress` first
   - If none, look for `status: not_started` + dependencies complete
   - If still none, pick first story in sprint order
   - NEVER fail with "no in_progress stories"

**Output:**

- Environment verified ✅
- Story selected with ID
- Initial state logged

---

### Step 02: MEMORY_LOAD

**Purpose:** Load relevant past context

**Actions:**

```json
{
  "server": "user-neo4j-memory",
  "toolName": "memory_search",
  "arguments": {
    "query": "Ralph failure OR Sprint 2 OR content population OR boundary OR verification",
    "limit": 10
  }
}
```

**Display results:**

```
📥 MEMORY LOAD:
- Found: [N] relevant memories
- Key insight: "Claimed 33 stories, reality 0 visible"
- Lesson: Must verify at every boundary
```

**If 0 results:**

```
⚠️ Proceeding without historical context
Risk: May repeat previous failures
```

---

### Step 03: STORY_SELECT

**Purpose:** Parse story and identify tasks

**Actions:**

1. **Load story file:**
   - Read COMPLETE story markdown
   - Parse all sections (AC-1 through AC-N)

2. **Identify task layers:**

   ```yaml
   Layer 1: Component Build
   Layer 2: CMS Registration
   Layer 3: Content Population
   Layer 4: Visual Verification
   ```

3. **Check current progress:**
   - Which layers already complete?
   - What's pending?
   - Where did previous attempt fail?

4. **Select next task:**
   - First incomplete task
   - Never skip layers

**Output:**

- Task selected with layer identified
- Previous layer status known

---

### Step 04: IMPLEMENT

**Purpose:** Execute task with layer awareness

**Actions:**

**For each layer:**

#### Layer 1: Component Build

1. Write failing test first
2. Implement component
3. Refactor while tests green
4. Verify: `pnpm tsc --noEmit`

#### Layer 2: CMS Registration

1. Add block to Pages collection
2. Generate types
3. Verify block appears in Admin UI

#### Layer 3: Content Population

1. **STOP - Do NOT auto-populate**
2. Report: `<promise>CMS_CONTENT_REQUIRED</promise>`
3. List what's needed:
   - Homepage global needs block array
   - Images need upload to Media collection
   - Content needs manual population
4. Verify what's already there:
   - Query DB: Does homepage global exist?
   - Query API: Does /api/globals/homepage return data?

#### Layer 4: Visual Verification

1. Screenshot homepage
2. Check for brand keywords
3. If template detected: FAIL

**Critical Rule:**

> If Layer 3 is incomplete, do NOT proceed to Layer 4.

---

### Step 05: TEST

**Purpose:** Run tests in Docker

**Pre-flight:**

```bash
docker-compose ps | grep ddpay-app-1
```

**Run tests:**

```bash
# Type check (MUST PASS)
docker-compose exec app pnpm tsc --noEmit

# Unit tests (MUST PASS)
docker-compose exec app pnpm exec vitest run

# Integration tests (NEW in V5)
docker-compose exec app pnpm exec vitest run integration

# E2E tests (if configured)
docker-compose exec app sh -c "test -f playwright.config.ts && pnpm exec playwright test || echo 'No E2E'"
```

**Note:** Tests passing ONLY validates Layer 1 (code).

---

### Step 06: BOUNDARY_VERIFICATION (NEW V5)

**Purpose:** Verify data crosses all boundaries

**Actions:**

#### 6A: Code → Database Boundary

```bash
# Check if component is registered in Payload config
grep -r "heroCarousel" src/collections/**/*.ts

# Check if block type exists in generated types
grep -r "HeroCarouselBlock" src/payload-types.ts
```

#### 6B: Database → API Boundary

```bash
# Test API returns data
curl -s http://localhost:3421/api/globals/homepage | jq .

# Expected: {"layout": [...blocks...]}
# If empty: CMS content not populated
```

#### 6C: API → UI Boundary

```bash
# Screenshot homepage
docker-compose exec app npx playwright screenshot \
  --viewport-size=1280,720 \
  http://localhost:3421 \
  verification.png

# Check for brand keywords
if grep -q "Difference Driven\|Empowering" verification.png 2>/dev/null; then
  echo "✅ Brand content detected"
else
  echo "❌ TEMPLATE DETECTED"
fi
```

#### 6D: Image Bridge Verification (NEW)

```bash
# List images in public/
ls public/images/ | wc -l

# List images in Media collection (via API)
curl -s http://localhost:3421/api/media | jq '.totalDocs'

# If public > Media: Gap detected
# Images exist in filesystem but not in CMS
```

---

### Step 07: VALIDATE

**Purpose:** Four-layer completion check

**Checklist:**

```
Layer 1: Component Build
  □ Files exist at correct paths
  □ TypeScript compiles
  □ Unit tests pass

Layer 2: CMS Registration
  □ Block in collection config
  □ Types generated
  □ Block appears in Admin UI

Layer 3: Content Population
  □ Homepage global exists in DB
  □ Layout array populated
  □ Blocks have content
  □ Images in Media collection

Layer 4: Visual Verification
  □ Screenshot taken
  □ Brand content visible
  □ No template indicators
  □ Visual match > 80%
```

**Output:**

- Layer status for each
- Pass/Fail for each boundary

---

### Step 08: COMMIT

**Purpose:** Record completion with truth

**When ALL layers pass:**

1. **Update progress.txt:**

   ```yaml
   stories:
     - id: story-X-Y
       status: complete
       layers_complete: [1, 2, 3, 4]
       boundary_checks:
         code_to_db: pass
         db_to_api: pass
         api_to_ui: pass
         image_bridge: pass
       visual_match_percent: 85
       components_built: 1
       cms_populated: 1
       user_visible: 1
   ```

2. **Stage and commit:**

   ```bash
   git add -A
   git commit -m "story-X-Y: Complete all 4 layers with boundary verification

   - Layer 1: Component built and tested
   - Layer 2: CMS registration complete
   - Layer 3: Content populated in Homepage global
   - Layer 4: Visual verification 85% match
   - Boundary checks: All passed
   - Truth: user_visible = 1"
   ```

3. **Log to Neo4j:**
   ```json
   {
     "event": "RALPH_STORY_COMPLETE",
     "story_id": "story-X-Y",
     "layers": [1, 2, 3, 4],
     "boundary_checks": "all_pass",
     "visual_match": 85,
     "user_visible": true
   }
   ```

---

## V5 Output Contract

### COMPLETED (All 4 Layers + All Boundaries)

```
<promise>COMPLETED</promise>
Story: story-X-Y
Layers: [1, 2, 3, 4]
Boundaries: [code_db, db_api, api_ui, image_bridge] = ALL PASS
Visual Match: 85%
Components Built: 1
CMS Populated: 1
User Visible: 1
Screenshot: verification.png
Commit: <hash>
```

### PARTIAL (Layer 1-2 Only)

```
<promise>PARTIAL_COMPLETE</promise>
Story: story-X-Y
Layers: [1, 2]
Layers Pending: [3, 4]
Status: Component built, CMS content required
Components Built: 1
CMS Populated: 0
User Visible: 0
```

### CMS_CONTENT_REQUIRED

```
<promise>CMS_CONTENT_REQUIRED</promise>
Story: story-X-Y
Layer: 3 (Content Population)
Issue: Homepage global not populated
Required Actions:
  1. Access Payload Admin /admin
  2. Edit Homepage global
  3. Add blocks to layout
  4. Populate with real content
  5. Upload images to Media collection
  6. Publish changes
Do Not: Auto-populate (human task)
```

### BOUNDARY_FAIL

```
<promise>BOUNDARY_FAIL</promise>
Story: story-X-Y
Boundary: db_to_api
Issue: /api/globals/homepage returns empty layout
Root Cause: CMS content not linked to homepage global
Action: Populate Homepage global in Payload Admin
```

### VISUAL_MISMATCH

```
<promise>VISUAL_MISMATCH</promise>
Story: story-X-Y
Expected: 80%+ brand content
Actual: Template showing
Issue: Content exists in CMS but not rendering
Action: Check component props, verify data binding
```

### IMAGE_BRIDGE_GAP

```
<promise>IMAGE_BRIDGE_GAP</promise>
Story: story-X-Y
Issue: 65 images in public/, 0 in Media collection
Gap: Images exist in filesystem but not CMS
Action: Upload images via Payload Admin Media collection
Do Not: Copy from public/ (won't work)
```

---

## V5 Pre-Flight Checklist

```bash
□ Correct worktree: pwd | grep ddpay-sprint
□ Docker running: docker-compose ps | grep ddpay
□ Images available: ls public/images/ | wc -l (expect 65+)
□ Admin accessible: curl -s http://localhost:3420/admin | grep -q Payload
□ API responding: curl -s http://localhost:3421/api/globals/homepage | jq .
□ Previous lessons loaded: memory search completed
```

---

## V5 Metrics (Truth-in-Reporting)

**Report these separately:**

| Metric           | Description                | V3 Value | V5 Target |
| ---------------- | -------------------------- | -------- | --------- |
| components_built | Code exists, compiles      | 33       | 33        |
| cms_registered   | Block in collection config | 33       | 33        |
| cms_populated    | Content in Homepage global | 0        | 33        |
| user_visible     | Brand content on screen    | 0        | 33        |

**Golden Rule:**

> A story is NOT complete until user_visible = 1

---

## V5 Persona Update

**Ralph's core instruction:**

```
OLD:
  "Implement all tasks in the story file"

NEW:
  "Implement AND verify all tasks in the story file.
   Verification is not optional.
   A task is not complete until its verification passes.

   Verify at every boundary:
   - Code → Database: Block registered?
   - Database → API: Content returns?
   - API → UI: User sees it?

   Report truth:
   - components_built (what you wrote)
   - cms_populated (what's in database)
   - user_visible (what user sees)"
```

---

## V5 Documentation Structure

### Quick Reference (1 page)

```
Ralph V5 Quick Start:
1. Run pre-flight
2. Load memory
3. Select story
4. Implement layer by layer
5. Verify at EVERY boundary
6. Report truth (3 metrics)
7. Commit
```

### Troubleshooting Guide

```
When X fails:
- Layer 3 fails → Check CMS Admin
- Boundary db→api fails → Check Homepage global
- Visual mismatch → Check content population
- Image gap → Upload to Media collection
```

### Full Specification

```
- This document (complete state machine)
- All boundary check scripts
- Integration test patterns
- Error handling matrix
```

---

## V5 Phased Implementation

### Phase 1: Quick Wins (1 sprint)

- [ ] Update Ralph persona to "implement AND verify"
- [ ] Add boundary check script (Section 06)
- [ ] Split progress reporting (components vs visible)

### Phase 2: Medium Effort (2 sprints)

- [ ] Add API verification step
- [ ] Add database query verification
- [ ] Update Definition of Done
- [ ] Create troubleshooting guide

### Phase 3: Hard (3 sprints)

- [ ] Add integration tests crossing boundaries
- [ ] Build CMS state verification automation
- [ ] Complete documentation rewrite
- [ ] Image bridge detection automation

---

## V5 Failure Handling

### "Tests pass but template showing"

- Detection: Screenshot lacks brand keywords
- Action: Output `<promise>CMS_CONTENT_REQUIRED</promise>`
- Never mark complete with template visible

### "Images in public/ but not in Media"

- Detection: public/ count > Media API count
- Action: Output `<promise>IMAGE_BRIDGE_GAP</promise>`
- Require human to upload to CMS

### "API returns empty"

- Detection: /api/globals/homepage returns `{"layout": []}`
- Action: Output `<promise>CMS_CONTENT_REQUIRED</promise>`
- Point to Homepage global in Admin

### "Visual match < 80%"

- Detection: Screenshot diff below threshold
- Action: Output `<promise>VISUAL_MISMATCH</promise>`
- Report which elements missing

---

## Appendix: Boundary Check Scripts

### Script: verify_code_to_db.sh

```bash
#!/bin/bash
# Verify component registered in Payload config

COMPONENT=$1
FOUND=$(grep -r "$COMPONENT" src/collections/**/*.ts | wc -l)

if [ "$FOUND" -gt 0 ]; then
  echo "✅ COMPONENT_REGISTERED: $COMPONENT found in $FOUND collection files"
  exit 0
else
  echo "❌ COMPONENT_NOT_REGISTERED: $COMPONENT not found in collections"
  exit 1
fi
```

### Script: verify_db_to_api.sh

```bash
#!/bin/bash
# Verify CMS has content via API

URL="${1:-http://localhost:3421/api/globals/homepage}"
RESPONSE=$(curl -s "$URL")

if echo "$RESPONSE" | jq -e '.layout | length > 0' > /dev/null 2>&1; then
  COUNT=$(echo "$RESPONSE" | jq '.layout | length')
  echo "✅ API_HAS_CONTENT: $COUNT blocks in layout"
  exit 0
else
  echo "❌ API_EMPTY: No blocks in layout"
  exit 1
fi
```

### Script: verify_api_to_ui.sh

```bash
#!/bin/bash
# Verify UI renders content

SCREENSHOT="${1:-verification.png}"
BRAND_KEYWORDS="Difference Driven|Empowering|Communities"

if [ -f "$SCREENSHOT" ]; then
  # Use Playwright to extract text
  TEXT=$(node -e "
    const { chromium } = require('playwright');
    (async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      await page.setContent('<img src=\"file://$SCREENSHOT\">');
      console.log(await page.textContent('body'));
      await browser.close();
    })();
  " || echo "")

  if echo "$TEXT" | grep -qE "$BRAND_KEYWORDS"; then
    echo "✅ UI_HAS_BRAND: Brand keywords found"
    exit 0
  else
    echo "❌ UI_TEMPLATE: No brand keywords found"
    exit 1
  fi
else
  echo "❌ NO_SCREENSHOT: $SCREENSHOT not found"
  exit 1
fi
```

### Script: verify_image_bridge.sh

```bash
#!/bin/bash
# Verify images exist in both filesystem and CMS

PUBLIC_COUNT=$(ls public/images/ 2>/dev/null | wc -l)
MEDIA_COUNT=$(curl -s http://localhost:3421/api/media | jq '.totalDocs' 2>/dev/null || echo "0")

echo "Images in public/: $PUBLIC_COUNT"
echo "Images in Media: $MEDIA_COUNT"

if [ "$MEDIA_COUNT" -ge "$PUBLIC_COUNT" ]; then
  echo "✅ IMAGE_BRIDGE_OK: All public images in Media collection"
  exit 0
else
  GAP=$((PUBLIC_COUNT - MEDIA_COUNT))
  echo "❌ IMAGE_BRIDGE_GAP: $GAP images in public/ but not in Media"
  exit 1
fi
```

---

## Document Metadata

| Field    | Value                                       |
| -------- | ------------------------------------------- |
| Version  | 5.0.0                                       |
| Created  | 2026-02-19                                  |
| Based on | Ralph V3 learnings                          |
| Status   | Draft                                       |
| Owner    | BMAD Team                                   |
| Location | `_bmad/core/workflows/ralph-v5/workflow.md` |

---

## Changelog

| Version | Date       | Change                                            |
| ------- | ---------- | ------------------------------------------------- |
| 5.0.0   | 2026-02-19 | Initial V5 creation from party-mode brainstorming |
| 1.0.0   | 2026-02-14 | Original Ralph workflow                           |

---

# END OF WORKFLOW
