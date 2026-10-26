---
name: epic-authoring
description: "Create or update strategic Epics in Azure DevOps. Use when defining business or platform outcomes, scope, measures, dependencies, risks, or exit criteria."
---

# Epic authoring
**Trigger:** Create or update an Epic.
Read `.github/agile-product-manager/ado-board-settings.md` first. For new Epics, use `System.WorkItemType` and `System.State` from the `Epic Board Item` section. Use configured area/iteration defaults if valid for the Epic. Validate the type and state for the target project/process; ask for missing or invalid mappings rather than guessing.

Ask new/update; for update fetch ID and current fields first. Establish strategic problem, beneficiaries, intended measurable outcome, boundaries, business/platform value, success measures, constraints, dependencies, risks and expected time horizon. Use up to 10 focused questions and probe only unresolved gaps. Draft `templates/epic.md` with concise context, objective, scope, outcome measures and high-level acceptance/exit criteria. Do not prescribe feature-level implementation. Ask priority/size only if configured for Epics. Preview exact fields/links and obtain explicit approval before create/update. Verify result after publication.
