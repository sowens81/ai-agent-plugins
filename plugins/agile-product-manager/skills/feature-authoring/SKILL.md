---
name: feature-authoring
description: "Create or update outcome-focused Features in Azure DevOps. Use when defining feature capability, scope, acceptance criteria, priority, size, or Epic parentage."
---

# Feature authoring
**Trigger:** Create or update a Feature.
Read `.github/agile-product-manager/ado-board-settings.md` first. For new Features, use `System.WorkItemType` and `System.State` from the `Feature Board Item` section. Use configured area/iteration defaults if valid for the Feature. Validate the type and state for the target project/process; ask for missing or invalid mappings rather than guessing.

Ask new/update; retrieve existing item by ID on update. Establish parent Epic, user/platform capability, outcome, scope, affected consumers, boundaries, constraints, dependencies and verifiable completion. Draft `templates/feature.md` with 3–6 outcome-focused criteria; no task checklist. Verify parent ID and type. Ask priority/size when configured. Show complete Markdown draft, mappings and links; request explicit approval before publishing and re-read to verify. **Create/update a Feature work item, not an Epic.**
