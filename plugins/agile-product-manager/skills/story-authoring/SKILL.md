---
name: story-authoring
description: "Create or update outcome-led User Stories in Azure DevOps. Use when defining story outcomes, scope, acceptance criteria, priority, size, or parent and dependency links."
---

# Story authoring
**Trigger:** Create or update a User Story in Azure DevOps.

Before drafting, read `.github/agile-product-manager/ado-board-settings.md`. Use `System.WorkItemType` as the User Story work item type and `System.State` as its initial state for a new item; these are separate settings. Use `System.AreaPath` and `System.IterationPath` as defaults, and `Team Name` as context only. Validate the configured values for the target project/process; ask if missing or invalid. Do not overwrite type or state on an existing item unless requested.

1. Ask **new or update**. For update obtain ID, fetch item, preserve fields/links not explicitly changed.
2. Ask 5–10 qualifying questions, adapt to known information: who benefits (or direct technical objective); what changes; current problem; expected outcome; in/out of scope; success evidence; constraints; environments; impact on existing consumers; dependencies. Follow up only where outcome remains unclear.
3. Ask user to select priority **1 / 2 / 3 / 4** (1 highest). 
4. Ask size **XS / S / M / L / XL / XXL**.
5. Ask parent Epic/Feature ID (or explicit no parent if allowed), predecessor IDs, successor IDs (allow none). Fetch and validate IDs, avoid self-links and cycles; confirm any cross-project link.
6. Draft via `templates/user-story.md`; use 3–6 measurable/observable criteria, not implementation subtasks. Distinguish story-specific acceptance from team DoD.
7. Show proposed title, description Markdown, acceptance criteria Markdown, priority, size, area, iteration and relation changes. Ask explicit publish approval.
8. Invoke `ado-board-items` skill to write, re-read and verify. Existing item updates must use revision check.

**Special cases:** For purely technical maintenance, use a direct objective, not an artificial persona. If work is just an activity, recommend a Task instead of a Story. Do not assume a work item type named `User Story` exists; resolve configured type or process-specific equivalent.
