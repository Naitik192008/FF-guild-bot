# config.py

# Guild Settings
TARGET_GUILD_ID = "3051009449"  # REPLACE THIS with your Guild ID
TARGET_GUILD_NAME = "Crimson Aura"

# Game Settings
PACKAGE_NAME = "com.dts.freefiremax"
ACTIVITY_NAME = "com.dts.freefireth/com.dts.freefireth.FFMainActivity"

import os

# ADB Settings
ADB_HOST = os.getenv("ADB_HOST", "127.0.0.1")
ADB_PORT = 5037

# Coordinates (960x540 Resolution)
# You may need to adjust these using "Pointer Location" in Developer Options
COORDS = {
    "START_MATCH": (850, 480),
    "GUILD_ICON": (910, 250),
    "SEARCH_BAR": (200, 100),
    "CONFIRM_JOIN": (480, 400),
    "EXIT_TO_LOBBY": (800, 450),
    "CONFIRM_EXIT": (480, 320),
    "SQUAD_MODE": (800, 350), # Example location for mode selection
    "INVITE_FRIEND": (900, 200)
}