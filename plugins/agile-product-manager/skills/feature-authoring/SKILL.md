---
name: feature-authoring
description: "Define or update Azure DevOps Features that specify a capability to deliver—such as infrastructure, platform, or product functionality—and how it contributes to a parent Epic's strategic outcome."
---

# Feature authoring

## Purpose

Define a capability that must be delivered to contribute to its parent Epic's strategic outcome. A capability may be infrastructure, platform, product functionality, or another coherent ability. A Feature describes what capability is needed and how it will be verified, not a list of implementation tasks.

## Workflow

1. Read `.github/agile-product-manager/ado-board-settings.md`. For a new Feature, use `System.WorkItemType` and `System.State` from the `Feature Board Item` section, plus configured area/iteration defaults when valid. Validate the mappings for the target project and process; ask if missing or invalid.
2. Establish whether this is a new Feature or an update. For an update, retrieve the item by ID first and preserve existing content, fields, and links unless the user asks to change them.
3. Identify and validate the parent Epic. Read its strategic outcome and measures. If there is no parent Epic, ask whether to select one or whether this Feature is intentionally standalone. Clarify:
   - What capability is needed, and who or what will use it?
   - What need or constraint does this capability address?
   - How will delivering this capability contribute to the Epic's strategic outcome?
   - What observable behavior or conditions will demonstrate that the capability is delivered?
   - What is in scope or out of scope, and are there material dependencies or constraints?

   Ask only questions needed to resolve material gaps. Do not invent requirements or claim the Feature alone proves the Epic's strategic outcome.
4. Draft using `templates/feature.md`. State the capability and its contribution to the Epic near the top. Define 3–6 concise, verifiable acceptance criteria for the capability; keep implementation steps and task checklists out.
5. Verify that each criterion describes observable capability behavior or an agreed delivery condition, and that the parent Epic link is valid.
6. Show the title, capability, Epic contribution, scope, acceptance criteria, field mappings, and link changes. Ask for explicit approval of the exact draft before writing. Request approval again if the draft changes.
7. On approval, create or update the Feature through `ado-board-items`, then re-read and verify the saved item and report its ID and URL. Report errors and partial outcomes clearly.

## Guardrails

- Keep the Feature focused on one coherent capability, whether infrastructure, platform, or product functionality.
- Express what capability is needed, not a preferred design or an implementation plan, unless a technical constraint is required.
- Keep Feature acceptance criteria distinct from the parent Epic's strategic success measures.
- Ask for priority or size only when configured for Features; never infer them.
- Never silently change existing state, type, or content. Follow the ADO skill's approval and write-safety requirements.
