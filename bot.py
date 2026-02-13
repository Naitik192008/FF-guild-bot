import time
import logging
from ppadb.client import Client as AdbClient
import config

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FreeFireBot:
    def __init__(self, device_serial):
        self.client = AdbClient(host=config.ADB_HOST, port=config.ADB_PORT)
        self.device = self.client.device(device_serial)
        self.serial = device_serial
        self.status = "IDLE"

    def tap(self, x, y):
        """Executes a tap command at specific coordinates."""
        if self.device:
            self.device.shell(f"input tap {x} {y}")
            time.sleep(0.5) # Short delay between actions

    def launch_game(self):
        """Starts Free Fire Max."""
        self.status = "STARTING_GAME"
        logging.info(f"[{self.serial}] Launching Game...")
        self.device.shell(f"monkey -p {config.PACKAGE_NAME} -c android.intent.category.LAUNCHER 1")
        time.sleep(30) # Wait for load (Adjust based on PC speed)
        
        # Handle "Tap to Begin"
        self.tap(480, 270) # Center screen
        time.sleep(15) # Wait for lobby

    def join_target_guild(self):
        """Automates the process of joining a specific Guild ID."""
        self.status = "JOINING_GUILD"
        logging.info(f"[{self.serial}] Attempting to join guild: {config.TARGET_GUILD_ID}")
        
        # 1. Open Guild Menu
        self.tap(*config.COORDS["GUILD_ICON"]) 
        time.sleep(2)
        
        # 2. Tap Search Box (Logic simplified for demo)
        # Real implementation requires handling the keyboard input
        self.device.shell(f"input text {config.TARGET_GUILD_ID}")
        time.sleep(1)
        
        # 3. Tap Join
        self.tap(*config.COORDS["CONFIRM_JOIN"])
        time.sleep(2)
        
        self.status = "GUILD_JOINED"
        logging.info(f"[{self.serial}] Join Guild Sequence Completed.")

    def farm_glory(self, loops=10):
        """
        Main loop for farming glory.
        To hit 40k points, this should ideally be run in 'Squad' mode with other bots.
        """
        self.status = "FARMING"
        for i in range(loops):
            logging.info(f"[{self.serial}] Starting Match {i+1}/{loops}")
            
            # Start Match
            self.tap(*config.COORDS["START_MATCH"])
            
            # Simulate Match Duration (Survival Time)
            # In a real scenario, use OCR/OpenCV to detect death/booyah
            match_duration = 600 # 10 minutes
            time.sleep(match_duration)
            
            # Return to Lobby
            self.tap(*config.COORDS["EXIT_TO_LOBBY"])
            time.sleep(2)
            self.tap(*config.COORDS["CONFIRM_EXIT"])
            time.sleep(10) # Loading back to lobby

        self.status = "IDLE"

# Helper to get all connected devices
def get_all_bots():
    client = AdbClient(host=config.ADB_HOST, port=config.ADB_PORT)
    devices = client.devices()
    return [FreeFireBot(device.serial) for device in devices]