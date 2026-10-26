# AI Agile Product Manager Helper

A portable, Markdown-first AI marketplace plugin for building an outcome-led engineering and platform backlog in Azure DevOps Boards.

## Contents

- `plugin.json`: Agent Plugins 1.1.0 portable manifest.
- `com.github.copilot/agents/backlog-manager.agent.md`: Copilot-specific conversational orchestrator and approval gates.
- `com.github.copilot/commands/`: Copilot-specific entry-point prompts for epic, feature, story, decomposition and board operations.
- `skills/*/SKILL.md`: reusable workflows and API guidance.
- `templates/`: concise item templates and quality checklist.
- `.github/agile-product-manager/ado-board-settings.md`: consumer configuration (copy into the consumer repository).
- `scripts/ado_wit.py`: dependency-free REST CLI, Azure CLI or PAT auth.

## Installation

Install the plugin directory as a plugin package. Agent Plugins 1.1.0 discovers the root `plugin.json` and skills under `skills/`. Agent and command files are host-specific extensions and are not portable core component types in Agent Plugins 1.1.0. Copy `.github/agile-product-manager/ado-board-settings.md` to the **consumer repository** and fill it in.

## Usage

1. Invoke `story`, `feature`, `epic`, `breakdown-epic`, `breakdown-feature` or `board` through your AI harness.
2. The agent reads the consumer settings and interviews the consumer before drafting.
3. Approve the exact proposed work item, fields and links before publication.
4. The ADO skill handles reads/writes; no write without approval.

## Authentication

`az login` followed by `az account get-access-token --resource 499b84ac-1321-427f-aa17-267ca6975798` (Azure DevOps resource), or export `AZURE_DEVOPS_PAT` in your shell. Never place tokens in settings, prompts, source control or logs. The script prefers PAT when present; otherwise uses Azure CLI. Ensure the identity has appropriate Boards permissions.

## CLI examples

```bash
python3 scripts/ado_wit.py auth-check
python3 scripts/ado_wit.py get 123
python3 scripts/ado_wit.py create 'User Story' --json proposed-item.json
python3 scripts/ado_wit.py update 123 --json proposed-item.json --rev 4
python3 scripts/ado_wit.py link 123 456 parent --rev 4
python3 scripts/ado_wit.py delete 123 --confirm-id 123
```

The CLI reads `ADO_ORG_URL` and `ADO_PROJECT` environment variables; `--json` is a path to a JSON document with `fields`, `markdown_fields` and optional `relations` (see `templates/payload.example.json`). Use `--dry-run` to preview write operations. The conversational agent must request explicit approval before executing writes, even if the CLI permits them.

## Design principles

Outcome-first with justified implementation constraints; 3–6 observable acceptance criteria; no forced persona for technical work; technical tasks separated from story outcomes; shared Definition of Done; concise UK English. Use Given/When/Then only for behavioural workflows.
