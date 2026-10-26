# sowens81-ai-plugins

The official [sowens81](https://github.com/sowens81) AI plugins marketplace ✨

## How to use the Market Place

### Visual Studio Code

1. Make sure you are signed in to GitHub Copilot and using a VS Code version that supports agent plugins.
2. Register this marketplace in your VS Code `settings.json`:

   ```json
   {
     "chat.plugins.enabled": true,
     "chat.plugins.marketplaces": [
       "sowens81/sowens81-ai-plugins"
     ]
   }
   ```

   Alternatively, open the Extensions view, search for `@agentPlugins`, and use the marketplace controls to add or browse a marketplace.
3. Open the Extensions view, search for `@agentPlugins`, browse **sowens81-ai-plugins**, and install **agile-product-manager**. You can also install it from the Agent Customizations editor under **Plugins**.
4. Review and fill in the plugin's Azure DevOps settings file in the consumer repository before using workflows that access Boards.
5. Use the installed `backlog-manager` agent or invoke a task-specific workflow such as `/story`, `/feature`, `/epic`, `/breakdown-epic`, `/breakdown-feature`, or `/board`. The plugin asks you to approve proposed changes before it writes to Azure DevOps.

### Github Copilot Cli

1. Install and authenticate GitHub Copilot CLI, then start it in the repository where you want to use the plugin.
2. Register this marketplace from your terminal:

   ```bash
   copilot plugin marketplace add sowens81/sowens81-ai-plugins
   ```

3. Browse and install the plugin:

   ```bash
   copilot plugin marketplace browse sowens81-ai-plugins
   copilot plugin install agile-product-manager@sowens81-ai-plugins
   ```

4. Check the installation with `copilot plugin list`, then start `copilot` in your target repository. In the interactive CLI, select the `backlog-manager` agent with `/agent`, or ask Copilot to use it. You can also invoke workflows such as `/story`, `/feature`, `/epic`, `/breakdown-epic`, `/breakdown-feature`, and `/board`.
5. Configure the Azure DevOps settings in the repository where you will use the plugin and sign in with an Azure DevOps identity that has the required Boards permissions. Review and approve each proposed write.

To install directly from the Git repository without registering the marketplace, use `/plugin install https://github.com/sowens81/ai-agent-plugins/tree/main/plugins/agile-product-manager`.

## 🔌 What's Inside

- **[agile-product-manager](./plugins/agile-product-manager/README.md)** — Reusable skills for drafting and creation an agile backlog consisting of epic, features and user stories. A custom agent with commands, configured to work with Github Copilot agent harness.

## 🌐 External Plugins

This marketplace also references plugins hosted in other repositories:

- **n/a**

## 📄 License

This project is licensed under the [MIT License](LICENSE).
