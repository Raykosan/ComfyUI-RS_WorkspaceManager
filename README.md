# 🦊 ComfyUI-RS_WorkspaceManager  

[![License: MIT](https://img.shields.io/badge/License-APACHE2.0-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-custom--node-orange)](https://github.com/comfyanonymous/ComfyUI)

**A powerful, standalone utility extension for ComfyUI designed to manage your entire workspace. Group multiple workflows into single-click Presets, backup your Interface Settings.**  

<img width="1384" height="832" alt="Screenshot_1" src="https://github.com/user-attachments/assets/1ad862f2-ad5e-4fc2-8f90-a11ed66b6df3" />

---

<img width="94" height="48" alt="Screenshot_2" src="https://github.com/user-attachments/assets/664ee29f-2462-4c20-842d-e11b6d684e4b" />

---

<img width="474" height="969" alt="Screenshot_3" src="https://github.com/user-attachments/assets/43cc5b42-7843-409e-8950-e64626068946" />

---

<img width="388" height="310" alt="Screenshot_4" src="https://github.com/user-attachments/assets/b947815c-c8ba-4d89-9066-6e0561b7d41a" />

---
---

## ✨ Features  
### 📂 Workflow Presets  
- **Save Tabs as Presets**: Group multiple open workflow tabs (e.g., Base Workflow, Upscaler, Face Detailer) into a single preset.  
- **One-Click Load**: Open all workflows from a preset instantly as new tabs.  
- **Smart Filtering**: Automatically ignores Unsaved Workflow tabs to keep your presets clean.  
- **Easy Updates**: Update your active preset with new changes (added/removed nodes) directly from the manager.  
- **Safe Replacement**: Loading a preset safely closes old tabs without breaking ComfyUI's internal state, while preserving your unsaved drafts.  

### ⚙️ Interface Settings Backup  
- **Save Configuration**: Backup your entire comfy.settings.json (UI layout, node preferences, etc.) to your local drive.  
- **Easy Restore**: Restore any previous backup with a single click.  
- **Built-in Restart**: The extension handles the ComfyUI server restart and automatically refreshes the page when it's back online.  

## 📦 Installation  
Set of nodes can be installed in several ways:  
- Clone repository to `ComfyUI/custom_nodes/` folder:  
```
git clone https://github.com/Raykosan/ComfyUI-RS_WorkspaceManager.git  
```
- Download the ZIP, unzip and put ComfyUI-RS_WorkspaceManager folder to: ComfyUI/custom_nodes/  

## 🔄 Migrating from ComfyUI_RaykoStudio  
### ⚠️ IMPORTANT FOR EXISTING USERS  
If you previously used the Workspace Manager built into the ComfyUI_RaykoStudio package, your presets will be automatically migrated when you first launch this standalone extension!  
However, to ensure 100% data safety, we recommend doing a manual backup before updating the old package:  
Go to ComfyUI/custom_nodes/ComfyUI_RaykoStudio/.  
Copy the presets_workflow folder to a safe place (e.g., your Desktop).  
Update ComfyUI_RaykoStudio (or delete it if you don't use its nodes).  
Install ComfyUI-RS_WorkspaceManager.  
Move your saved presets_workflow folder into the new ComfyUI-RS_WorkspaceManager directory.  

## 🚀 How to Use  
### Enabling the Topbar Icons  
Go to ComfyUI Settings (⚙️).  
Scroll down to the RS Workspace Manager section.  
Check the "Show icon in top menu" box.  
Look at the top menu (next to the RUN button). You will see two new buttons:  
🖥️ Settings Manager — Opens the main interface.  
🗑️ Close All Workflows — Instantly closes all open tabs safely (keeps a fresh Unsaved draft).  

### Managing Workflow Presets  
Open the Settings Manager (🖥️).  
Open the workflow tabs you want to group together.  
Type a name in the "Save New Preset" field and click 💾 Save as New Preset.  
A green banner will appear: Active Preset: "Your Name".  
To update it later, click 💾 Update Current Preset.  
To load a preset, click 📂 Show Presets and click Load next to the desired preset.  

### Managing Interface Settings  
In the Save Interface Settings block, enter a custom name for your backup.  
Click 💾 Save Settings.  
To restore, click 📂 Load Backups, find your backup, and click ✓ Restore. Follow the prompts to restart the server.  

## 📁 File Structure  
### Workflow Presets:  
Stored locally inside the extension folder. These are lightweight JSON files containing the paths to your workflows.  
`ComfyUI/custom_nodes/ComfyUI-RS_WorkspaceManager/presets_workflow/`  

### Interface Backups:  
Stored outside the ComfyUI directory in your user Documents folder to keep your installation clean.  
`C:/Users/USER/Documents/ComfyUI_Settings_Backups/` 

## 🛠️ Technical Notes  
Browser Storage Management: The extension monkey-patches localStorage.setItem to catch QuotaExceededError. If your browser storage is full, it will automatically delete old drafts from closed tabs and retry the save.  
Active Preset Tracking: The extension uses sessionStorage to remember your active preset. Refreshing the page keeps the state, but closing the browser resets it.  
Restarting the Server: The extension uses os.execv to restart the Python server. If you are using a third-party launcher (like Stability Matrix or Pinokio), the server might close but not automatically reopen. In this case, simply restart your launcher manually.  

## 📝 License  
This project is licensed under the Apache License 2.0. See the LICENSE file for details.  

