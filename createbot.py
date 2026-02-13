import time
import config
import logging
from ppadb.client import Client as AdbClient

def create_fresh_bot(device):
    """Resets the Free Fire guest account on the given device."""
    try:
        logging.info(f"[{device.serial}] Wiping old guest account...")
        
        # 1. Force Stop Game
        device.shell(f"am force-stop {config.PACKAGE_NAME}")
        
        # 2. Delete Guest Account Credentials
        device.shell(f"rm -rf /data/data/{config.PACKAGE_NAME}/shared_prefs/com.garena.msdk.xml")
        device.shell("rm -rf /sdcard/com.garena.msdk")
        
        # 3. Launch Game
        logging.info(f"[{device.serial}] Launching to create new Guest...")
        device.shell(f"monkey -p {config.PACKAGE_NAME} -c android.intent.category.LAUNCHER 1")
        
        # 4. Wait needed (manual tap or automated if implemented)
        # Note: Tapping logic would need checking screen state which is complex without OpenCV
        # For now, we launch and let the user handle the initial tap or add a blind tap
        time.sleep(20)
        # device.shell("input tap 480 270") # Optional: Try to center tap
        
        logging.info(f"[{device.serial}] Reset complete. Game launched.")
        
    except Exception as e:
        logging.error(f"[{device.serial}] Error creating fresh bot: {e}")
    