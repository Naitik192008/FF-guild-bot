from flask import Flask, render_template, request, jsonify
from bot import get_all_bots, FreeFireBot
import threading

app = Flask(__name__)

# Global dictionary to keep track of bot instances
active_bots = {} 

def refresh_bots():
    """Scans for ADB devices and updates the active_bots list."""
    try:
        bots = get_all_bots()
        if bots:
            for bot in bots:
                if bot.serial not in active_bots:
                    active_bots[bot.serial] = bot
    except Exception as e:
        print(f"Error connecting to ADB: {e}")

@app.route('/')
def index():
    refresh_bots()
    return render_template('dashboard.html', bots=active_bots.values())

@app.route('/api/join_guild', methods=['POST'])
def api_join_guild():
    """Trigger all bots to join the target guild defined in config."""
    refresh_bots()
    count = 0
    for serial, bot in active_bots.items():
        # Run in a separate thread to not block the UI
        t = threading.Thread(target=bot.join_target_guild)
        t.start()
        count += 1
    return jsonify({"status": "success", "message": f"Command sent to {count} bots."})

@app.route('/api/start_farming', methods=['POST'])
def api_start_farming():
    """Trigger all bots to start the farming loop."""
    refresh_bots()
    count = 0
    for serial, bot in active_bots.items():
        t = threading.Thread(target=bot.farm_glory, args=(50,)) # 50 loops
        t.start()
        count += 1
    return jsonify({"status": "success", "message": f"Farming started on {count} bots."})

@app.route('/api/create_bots', methods=['POST'])
def api_create_bots():
    """Trigger all bots to reset and create a fresh guest account."""
    refresh_bots()
    count = 0
    from createbot import create_fresh_bot # Import here to avoid circular dependencies if any
    
    for serial, bot in active_bots.items():
        # Using the raw device object from the bot wrapper if available, or passing the wrapper if it has necessary methods
        # The bot.py wrapper has .device attribute
        target_device = bot.device 
        
        t = threading.Thread(target=create_fresh_bot, args=(target_device,))
        t.start()
        count += 1
    return jsonify({"status": "success", "message": f"Bot creation started on {count} devices."})

if __name__ == '__main__':
    # Initialize connection
    refresh_bots()
    print(f"Found {len(active_bots)} devices.")
    try:
        app.run(debug=True, port=5000)
    except Exception as e:
        print(f"Error starting app: {e}")