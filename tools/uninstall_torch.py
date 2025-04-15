"""
uninstall_torch.py

Cross-platform uninstaller script to fully remove PyTorch and related packages.
Detects Windows or Linux/macOS and performs relevant uninstallation steps.

Usage:
    python tools/uninstall_torch.py
"""

import subprocess
import sys
import platform
import os

def uninstall_packages():
    packages = ["torch", "torchvision", "torchaudio", "easyocr", "pytesseract"]
    print("\nUninstalling PyTorch and related packages...")
    for pkg in packages:
        subprocess.run([sys.executable, "-m", "pip", "uninstall", pkg, "-y"])

def clear_cache():
    system = platform.system()
    print("\nClearing cache (if exists)...")
    if system == "Windows":
        subprocess.run(["cmd", "/c", "rmdir /S /Q %LOCALAPPDATA%\\torch"], shell=True)
        subprocess.run(["cmd", "/c", "rmdir /S /Q %LOCALAPPDATA%\\pip\\cache"], shell=True)
    else:
        subprocess.run(["rm", "-rf", os.path.expanduser("~/.cache/torch")])
        subprocess.run(["rm", "-rf", os.path.expanduser("~/.cache/pip")])

def confirm_removal():
    print("\nVerifying...")
    result = subprocess.run([sys.executable, "-m", "pip", "list"], capture_output=True, text=True)
    if "torch" not in result.stdout:
        print("✅ PyTorch has been successfully removed.")
    else:
        print("❌ PyTorch still appears to be installed.")

if __name__ == "__main__":
    print("LiftOCR PyTorch Uninstaller")
    print("---------------------------")
    uninstall_packages()
    clear_cache()
    confirm_removal()
