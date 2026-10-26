# Agile Product Manager

An outcome-led backlog assistant for Azure DevOps Boards. It provides skills for authoring Epics, Features, and User Stories, decomposing backlogs, and reading or updating work items.

## Install in Visual Studio Code

1. Use a VS Code version with agent plugin support and sign in to GitHub Copilot.
2. Add this marketplace in VS Code `settings.json`:

   ```json
   {
     "chat.plugins.enabled": true,
     "chat.plugins.marketplaces": [
       "sowens81/ai-agent-plugins"
     ]
   }
   ```

3. Open **Extensions**, search for `@agentPlugins`, browse **sowens81-ai-plugins**, and install **agile-product-manager**. Alternatively, open **Chat: Open Customizations**, select **Plugins**, and install it from the marketplace.
4. Set up the consumer repository’s Azure DevOps settings as described below.
5. Use the `backlog-manager` agent or the `/story`, `/feature`, `/epic`, `/breakdown-epic`, `/breakdown-feature`, and `/board` workflows.

## Install in GitHub Copilot CLI

Run these commands in a terminal:

```bash
copilot plugin marketplace add sowens81/ai-agent-plugins
copilot plugin marketplace browse sowens81-ai-plugins
copilot plugin install agile-product-manager@sowens81-ai-plugins
copilot plugin list
```

Then start `copilot` in the repository where you want to use the plugin. Select `backlog-manager` with `/agent`, or invoke one of the workflows listed above. You can also install the plugin directly without registering the marketplace:

```bash
copilot plugin install sowens81/ai-agent-plugins:plugins/agile-product-manager
```

## Configure Azure DevOps Boards

The plugin’s settings file is read from the **consumer repository**, not from the plugin installation directory:

```text
.github/agile-product-manager/ado-board-settings.md
```

Copy the example from [`templates/ado-board-settings.example.md`](./templates/ado-board-settings.example.md) into that location, then replace example values with values valid for your Azure DevOps organization and project. The settings file is Markdown tables; preserve the `Name` and `Value` columns so the skills can identify each setting.

The current workspace’s [`ado-board-settings.md`](../../.github/agile-product-manager/ado-board-settings.md) provides a filled-in example. Settings mean:

| Setting | How the plugin uses it |
| --- | --- |
| `Team Name` | Team context for board-related questions. It is not an Azure DevOps work item field. |
| `System.AreaPath` | Default area path for new work items. |
| `System.IterationPath` | Default iteration path for new work items. |
| `System.WorkItemType` | Work item type listed in each item section (`Epic Board Item`, `Feature Board Item`, or `User Story Board Item`). |
| `System.State` | Initial state listed in that same item section, if valid for that type and process. |

The plugin selects the matching section for the item being created: Epic settings for Epics, Feature settings for Features, and User Story settings for User Stories. It checks that configured types, states, fields, area paths, and iteration paths are valid for the target project and work item type before writing. If a section or setting is missing, unsupported, or ambiguous, it asks rather than guessing. Existing work items retain their current type and state unless the user explicitly requests a change.

The settings file does not contain credentials, organization URL, or project name. Provide the latter two to the CLI through environment variables:

```bash
export ADO_ORG_URL="https://dev.azure.com/YOUR_ORGANIZATION"
export ADO_PROJECT="YOUR_PROJECT"
```

Authenticate with `az login` using an identity that has the required Azure DevOps Boards permissions. The CLI can obtain an Azure DevOps access token through Azure CLI. Alternatively, set `AZURE_DEVOPS_PAT` in the environment; do not put tokens in the Markdown settings file, prompts, or source control. Never print or store credentials in plugin files.

## Using the workflows

- **Create or update:** `/story`, `/feature`, or `/epic`
- **Decompose:** `/breakdown-epic` or `/breakdown-feature`
- **Read or manage board items:** `/board`

The authoring skills use the settings as defaults, interview you to resolve missing details, and preview exact field and relation changes. Explicitly approve the proposed write before it is made. Updates are read first and use revision checks; deletes require a separate approval.

## Included files

- `plugin.json`: Agent Plugins manifest.
- `skills/`: portable skills and Azure DevOps REST guidance.
- `com.github.copilot/`: Copilot-specific agent and workflow entry points.
- `templates/`: work item templates, payload example, quality checklist, and settings example.
- `scripts/ado_wit.py`: dependency-free Azure DevOps REST CLI.

The settings example and the user-specific settings are configuration aids, not credentials. The Azure DevOps token is supplied at runtime.
