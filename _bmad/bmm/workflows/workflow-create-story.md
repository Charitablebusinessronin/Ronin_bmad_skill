---
name: "create-story"
slug: "create-story"
type: "workflow"
---


# Notion AI System Instructions: Create Story

## Workflow Identity
**Name:** create-story
**Title:** Create User Story
**Module:** BMM (Business Method Module)
**Workflow Type:** BMAD

## Purpose
Create the next user story markdown from epics/PRD and architecture, using a standard template and saving to the stories folder.

## Description
Workflow for creating individual user stories from epics. Uses PRD, architecture, and epic definitions to create well-structured user stories with acceptance criteria, ready for development. Generates stories following standard templates and saves them in the appropriate location.

## How to Execute This Workflow in Notion

### Activation
When you need to create a new user story from an epic:
1. **Identify epic and story** to create
1. **Load context** (PRD, Architecture, Epic, Tech Spec)
1. **Create story page** in Notion
1. **Structure with acceptance criteria**

### Execution Steps in Notion
1. **Story Identification**
1. **Context Assembly**
1. **Story Creation**

### Natural Language Commands
- “Create story” or “Generate user story”
- “Draft story” or “Write user story”
- “Create story from epic” or “New story”

### Workflow Inputs
- Epics (required)
- PRD (required)
- Architecture (optional)
- Tech Spec (optional)

### Workflow Outputs
- User story document in Notion
- Acceptance criteria
- Links to epic and PRD

### Related Agents
- Scrum Master (primary)
- Product Manager (requirements)
- Developer (implementation reference)

---

## Integration Details
**Module:** BMM
**Phase Focus:** Implementation (Phase 4)
**Related Workflows:**
- create-epics-and-stories (input)
- dev-story (next step)
- story-context (preparation)
**Integration Points:** Notion
**Platform:** Claude (via Notion AI)
