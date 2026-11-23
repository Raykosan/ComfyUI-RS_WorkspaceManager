# SPDX-License-Identifier: Apache-2.0
# Copyright 2025-2026 Raykosan (RaykoStudio)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil
import logging
from . import settings_manager_api

logger = logging.getLogger(__name__)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CUSTOM_NODES_DIR = os.path.dirname(CURRENT_DIR)
OLD_PACKAGE_PATH = os.path.join(CUSTOM_NODES_DIR, "ComfyUI_RaykoStudio")

WEB_DIRECTORY = "./js"

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

def migrate_old_presets():
    new_presets_dir = os.path.join(CURRENT_DIR, "presets_workflow")
    old_presets_dir = os.path.join(OLD_PACKAGE_PATH, "presets_workflow")

    if not os.path.exists(old_presets_dir):
        return

    if not os.path.exists(new_presets_dir) or not os.listdir(new_presets_dir):
        try:
            shutil.copytree(old_presets_dir, new_presets_dir, dirs_exist_ok=True)
            logger.info("🦊 RS Workspace Manager: Successfully migrated presets from ComfyUI_RaykoStudio.")
        except Exception as e:
            logger.error(f"🦊 Failed to migrate old presets: {e}")

migrate_old_presets()

logger.info("🦊 RS Workspace Manager: module loaded successfully")

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]