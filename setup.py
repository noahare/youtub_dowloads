import os
import subprocess
import sys
import platform

def run_cmd(command):
    """Executes system commands and handles errors."""
    try:
        print(f"[*] Running: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error occurred while running: {command}\n{e}")

def initialize_environment():
    print("="*50)
    print("  UNIVERSAL SETUP FOR YOUTUBE DOWNLOADER PROJECT")
    print("="*50)

    # 1. Identify Environment
    os_name = platform.system().lower()
    is_termux = os.path.exists("/data/data/com.termux")
    
    print(f"[*] System Detected: {'Termux/Android' if is_termux else os_name.capitalize()}")

    # 2. Update and Install Python Dependencies
    print("[*] Updating pip and installing requirements...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    
    # Create requirements.txt dynamically if not exists
    if not os.path.exists("requirements.txt"):
        with open("requirements.txt", "w") as req:
            req.write("yt-dlp\n")
    
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    # 3. Handle FFmpeg Installation (Crucial for merging Video+Audio)
    print("[*] Checking for FFmpeg dependency...")
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[+] FFmpeg is already installed and configured.")
    except FileNotFoundError:
        print("[-] FFmpeg not found. Attempting auto-installation...")
        
        if is_termux:
            run_cmd("pkg update && pkg upgrade -y")
            run_cmd("pkg install ffmpeg -y")
        
        elif os_name == "linux":
            print("[!] Linux detected. Root privileges may be required.")
            run_cmd("sudo apt update && sudo apt install ffmpeg -y")
            
        elif os_name == "windows":
            print("[!] Windows detected. Attempting to install via winget...")
            run_cmd("winget install ffmpeg")
            print("[!] If winget fails, please download from: https://ffmpeg.org/download.html")

    print("\n" + "="*50)
    print("✅ SETUP COMPLETED SUCCESSFULLY!")
    print(f"Current Directory: {os.getcwd()}")
    print("You can now run: python yt.py")
    print("="*50)

if __name__ == "__main__":
    initialize_environment()
