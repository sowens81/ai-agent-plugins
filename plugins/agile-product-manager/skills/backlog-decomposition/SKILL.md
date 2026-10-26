---
name: backlog-decomposition
description: "Break down Azure DevOps Epics into Features and Stories, or Features into Stories, while preserving hierarchy, outcomes, dependencies, and existing children."
---

# Backlog decomposition
**Triggers:** Epic -> Features + Stories; Feature -> Stories.
Read `.github/agile-product-manager/ado-board-settings.md` before planning or creating children. Use `System.AreaPath` and `System.IterationPath` as defaults only after validating them for the target project. For each new Epic, Feature, or User Story, take `System.WorkItemType` and `System.State` from its matching `Epic Board Item`, `Feature Board Item`, or `User Story Board Item` section. Validate these mappings for the target project's process; if a section is missing or a setting invalid, ask rather than borrow another type's values or guess.

1. Retrieve source work item by ID, including current children, relations, scope and acceptance criteria.
2. Clarify intended outcomes, boundaries, consumer journeys, platform constraints and delivery sequencing. Do not duplicate existing child items.
3. Suggest a compact hierarchy: Epic > Features > Stories; Feature > Stories. Stories should be independently verifiable slices, not infrastructure tasks masquerading as stories.
4. For each child provide title, short objective, scope and 3–6 testable acceptance criteria. Highlight assumptions and proposed dependencies.
5. Present hierarchy and ask consumer to approve/revise. Then ask **separate explicit approval** for bulk publication with counts, fields, parents and dependency links.
6. Create parents before children; re-read IDs; add hierarchy and dependency links only when valid. On partial failure report created IDs and outstanding work; never auto-delete/rollback without approval.
7. Never mutate existing children or create duplicates without confirmation. Keep task-level implementation out of story criteria.
