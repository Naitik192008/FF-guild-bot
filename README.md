# Free Fire Max Guild Automation Suite

A Python-based automation tool for managing Free Fire Max guild activities. Supports both local execution (via USB) and cloud deployment (via Docker).

## Features
- **Auto Join Guild**: Bots automatically search and join your target guild.
- **Glory Farming**: Automated match recycling to farm guild glory.
- **Bot Creation**: Automatically wipes data to create new guest accounts.
- **Cloud Ready**: Runs entirely in the cloud with an emulated Android device.

---

## 🚀 Quick Start: Cloud Deployment (VPS)
**Run without any local device or ADB.**

### Prerequisites
1.  A **GitHub** account.
2.  A **Cloud VPS** (e.g., DigitalOcean, Vultr) with KVM support.
    *   *Note: Free PaaS tiers like Railway/Render will NOT work due to virtualization requirements.*

### Step-by-Step Setup
1.  **Prepare the Code**:
    Open a terminal in this folder and run:
    ```powershell
    .\setup_git.ps1
    ```
    *Follow instructions to push your code to GitHub.*

2.  **Deploy to VPS**:
    Log into your VPS and run:
    ```bash
    git clone <YOUR_REPO_URL>
    cd <REPO_NAME>
    chmod +x setup_vps.sh
    ./setup_vps.sh
    ```

3.  **Access Your Bot**:
    *   Open `http://<VPS_IP>:5000` to control the bot.
    *   Open `http://<VPS_IP>:6080` to see the Android screen.

---

## 📱 Local Setup (USB)
**Run on your PC with a physical phone or emulator (e.g., LDPlayer).**

### Prerequisites
1.  **Python 3.8+** installed.
2.  **Android Phone** connected via USB (Debugging ON) OR **Emulator** running.

### Step-by-Step Setup
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Verify Connection**:
    Ensure your device is listed:
    ```bash
    adb devices
    ```

3.  **Run the Bot**:
    ```bash
    python app.py
    ```

4.  **Access Dashboard**:
    Open your browser to: `http://127.0.0.1:5000`

---

## 🛠 Usage
**Create Bots**:
- Click **"Create/Reset Bots"** on the dashboard.
- This will WIPE the Free Fire data on connected devices and launch a fresh guest account.
- **Warning**: This is destructive! Only use on throwaway accounts.

**Join Guild**:
- Update `config.py` with your `TARGET_GUILD_ID`.
- Click **"Join Guild"** to command all bots to join.

**Farm Glory**:
- Click **"Start Farming"** to begin the match loop.
