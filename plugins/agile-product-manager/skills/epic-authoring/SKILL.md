---
name: epic-authoring
description: "Define or update strategic Azure DevOps Epics that state an engineering or organisational improvement and how success will be measured."
---

# Epic authoring

## Purpose

Create an Epic that communicates the strategic improvement the organisation or engineering team intends to achieve and the evidence that will show whether it succeeded. An Epic is an outcome, not a feature list, project plan, or implementation task.

## Workflow

1. Read `.github/agile-product-manager/ado-board-settings.md`. For a new Epic, use `System.WorkItemType` and `System.State` from the `Epic Board Item` section, and the configured area/iteration defaults when valid. Validate the mappings for the target project and process; ask if they are missing or invalid.
2. Establish whether this is a new Epic or an update. For an update, retrieve the item by ID first and preserve existing content, fields, and links unless the user asks to change them.
3. Ask focused questions to clarify:
   - What engineering or organisation improvement should result, and who benefits?
   - What problem or opportunity makes the improvement important now?
   - How will success be measured? Identify meaningful indicators and, where known, their baseline, target, measurement source, and timeframe.
   - What is in scope and explicitly out of scope?
   - Are there material constraints or dependencies?

   Ask only questions needed to resolve material gaps. Never invent a baseline, target, metric, deadline, or rationale; label unknowns and ask whether to leave them open.

4. Draft using `templates/epic.md`. Lead with one concise strategic outcome statement and make the success measures prominent. Keep scope at outcome/capability level; do not prescribe Features, technical design, or implementation tasks.
5. Review that each measure is observable and relevant to the stated improvement. Separate measures of delivered activity from measures of actual impact; do not present activity completion alone as proof of strategic success.
6. Show the proposed title, description, success measures, scope, relevant constraints/dependencies, field mappings, and link changes. Ask for explicit approval of the exact draft before writing. Request approval again if the draft changes.
7. On approval, create or update the Epic through `ado-board-items`, then re-read and verify the saved item and report its ID and URL. Report errors and partial outcomes clearly.

## Guardrails

- Keep the Epic focused on the strategic outcome and its measurement.
- Do not turn it into a backlog of Features or a delivery plan.
- Do not force a beneficiary persona for internal engineering or organisation improvements.
- Ask for priority or size only when configured for Epics; never infer them.
- Never silently change existing state, type, or content. Follow the ADO skill's approval and write-safety requirements.
