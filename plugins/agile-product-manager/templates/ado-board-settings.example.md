# ADO Board Settings

Replace each example value with one valid for the consumer's Azure DevOps organization and project. Keep the two-column `Name` and `Value` tables so the plugin skills can read the configuration.

## General Settings

| Name | Value |
| --- | --- |
| `Team Name` | `YOUR_TEAM` |
| `System.AreaPath` | `YOUR_PROJECT\\YOUR_AREA` |
| `System.IterationPath` | `YOUR_PROJECT\\YOUR_ITERATION` |

## Epic Board Item

| Name | Value |
| --- | --- |
| `System.WorkItemType` | `Epic` |
| `System.State` | `New` |

## Feature Board Item

| Name | Value |
| --- | --- |
| `System.WorkItemType` | `Feature` |
| `System.State` | `New` |

## User Story Board Item

| Name | Value |
| --- | --- |
| `System.WorkItemType` | `User Story` |
| `System.State` | `New` |

For each work item section, `System.WorkItemType` is the Azure DevOps work item type, not its state. `System.State` is the initial state for newly created items of that type. Validate every type and state against the consumer project's process. Do not put organization URLs, project credentials, access tokens, or PATs in this file.
