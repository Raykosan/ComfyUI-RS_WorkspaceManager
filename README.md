🦊 ComfyUI-RS_WorkspaceManager
https://img.shields.io/badge/ComfyUI-Custom_Node-blue
https://img.shields.io/badge/License-Apache_2.0-green
https://img.shields.io/badge/Version-1.0.0-orange

A powerful, standalone utility extension for ComfyUI designed to manage your entire workspace. Group multiple workflows into single-click Presets, backup your Interface Settings, and let the extension automatically clean up browser storage to prevent annoying "Failed to save workflow draft" errors.

✨ Features
📂 Workflow Presets
Save Tabs as Presets: Group multiple open workflow tabs (e.g., Base Workflow, Upscaler, Face Detailer) into a single preset.

One-Click Load: Open all workflows from a preset instantly as new tabs.

Smart Filtering: Automatically ignores Unsaved Workflow tabs to keep your presets clean.

Easy Updates: Update your active preset with new changes (added/removed nodes) directly from the manager.

Safe Replacement: Loading a preset safely closes old tabs without breaking ComfyUI's internal state, while preserving your unsaved drafts.

⚙️ Interface Settings Backup
Save Configuration: Backup your entire comfy.settings.json (UI layout, node preferences, etc.) to your local drive.

Easy Restore: Restore any previous backup with a single click.

Built-in Restart: The extension handles the ComfyUI server restart and automatically refreshes the page when it's back online.

🧹 Auto-Cleanup of Drafts (Background)
No More Storage Errors: ComfyUI saves drafts of your workflows in the browser's localStorage. This extension monitors storage limits and automatically cleans up orphaned drafts from closed tabs.

Prevents "Failed to save workflow draft" Popups: Works silently in the background to ensure ComfyUI always has enough space to save your current work.

📦 Installation
Navigate to your ComfyUI custom_nodes folder:

bash
cd ComfyUI/custom_nodes/
Clone this repository:

bash
git clone https://github.com/Raykosan/ComfyUI-RS_WorkspaceManager.git
Restart ComfyUI. (No additional Python dependencies are required).

🔄 Migrating from ComfyUI_RaykoStudio
⚠️ IMPORTANT FOR EXISTING USERS
If you previously used the Workspace Manager built into the ComfyUI_RaykoStudio package, your presets will be automatically migrated when you first launch this standalone extension!

However, to ensure 100% data safety, we recommend doing a manual backup before updating the old package:

Go to ComfyUI/custom_nodes/ComfyUI_RaykoStudio/.

Copy the presets_workflow folder to a safe place (e.g., your Desktop).

Update ComfyUI_RaykoStudio (or delete it if you don't use its nodes).

Install ComfyUI-RS_WorkspaceManager.

Move your saved presets_workflow folder into the new ComfyUI-RS_WorkspaceManager directory.

🚀 How to Use
Enabling the Topbar Icons
Go to ComfyUI Settings (⚙️).

Scroll down to the RS Workspace Manager section.

Check the "Show icon in top menu" box.

Look at the top menu (next to the RUN button). You will see two new buttons:

🖥️ Settings Manager — Opens the main interface.

🗑️ Close All Workflows — Instantly closes all open tabs safely (keeps a fresh Unsaved draft).

Managing Workflow Presets
Open the Settings Manager (🖥️).

Open the workflow tabs you want to group together.

Type a name in the "Save New Preset" field and click 💾 Save as New Preset.

A green banner will appear: Active Preset: "Your Name".

To update it later, click 💾 Update Current Preset.

To load a preset, click 📂 Show Presets and click Load next to the desired preset.

Managing Interface Settings
In the Save Interface Settings block, enter a custom name for your backup.

Click 💾 Save Settings.

To restore, click 📂 Load Backups, find your backup, and click ✓ Restore. Follow the prompts to restart the server.

📁 File Structure
Workflow Presets:
Stored locally inside the extension folder. These are lightweight JSON files containing the paths to your workflows.
ComfyUI/custom_nodes/ComfyUI-RS_WorkspaceManager/presets_workflow/

Interface Backups:
Stored outside the ComfyUI directory in your user Documents folder to keep your installation clean.
Documents/ComfyUI_Settings_Backups/

🛠️ Technical Notes
Browser Storage Management: The extension monkey-patches localStorage.setItem to catch QuotaExceededError. If your browser storage is full, it will automatically delete old drafts from closed tabs and retry the save.

Active Preset Tracking: The extension uses sessionStorage to remember your active preset. Refreshing the page keeps the state, but closing the browser resets it.

Restarting the Server: The extension uses os.execv to restart the Python server. If you are using a third-party launcher (like Stability Matrix or Pinokio), the server might close but not automatically reopen. In this case, simply restart your launcher manually.

📝 License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.

