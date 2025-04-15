""
"""
install_torch.py

Interactive installer script for LiftOCR to help users install the appropriate version
of PyTorch (torch, torchvision, torchaudio) based on their system configuration.

Features:
- Detects presence of an NVIDIA GPU
- Determines CUDA version via `nvidia-smi`
- Recommends the best-matching PyTorch version
- Offers CPU-only and manual installation options
- Maps CUDA version to known PyTorch wheel tags

Usage:
    python tools/install_torch.py
"""

import subprocess
import sys
import re

def has_nvidia_gpu():
    """Check if an NVIDIA GPU is available using nvidia-smi."""
    try:
        result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def get_cuda_version():
    """Parse the CUDA version from nvidia-smi output if available."""
    try:
        result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            match = re.search(r"CUDA Version: (\d+\.\d+)", line)
            if match:
                return match.group(1)
    except Exception:
        return None

# Map CUDA major versions to supported PyTorch wheel folders
CUDA_TO_TORCH_WHEEL = {
    "12": "cu121",
    "11": "cu118",
    "10": "cu102",
}

def install_pytorch(option, cuda_version=None):
    """
    Install the appropriate version of PyTorch based on user choice.

    Parameters:
    - option: str (user choice 1, 2, or 3)
    - cuda_version: str (parsed from system, e.g. "12.1")
    """
    if option == "1" and cuda_version:
        major = cuda_version.split(".")[0]
        wheel_tag = CUDA_TO_TORCH_WHEEL.get(major)
        if not wheel_tag:
            print(f"No known torch wheel for CUDA {cuda_version}. Defaulting to CPU-only.")
            option = "2"
        else:
            url = f"https://download.pytorch.org/whl/{wheel_tag}"
            cmd = [sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio", "--index-url", url]
            print("\nRunning:", " ".join(cmd))
            result = subprocess.run(cmd)
            if result.returncode == 0:
                return
            else:
                print("\n[ERROR] CUDA install failed. Falling back to CPU-only.")
                option = "2"

    if option == "2":
        cmd = [sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio"]
        print("\nRunning:", " ".join(cmd))
        subprocess.run(cmd)

    elif option == "3":
        manual = input("Paste your custom pip install command:\n")
        cmd = manual.strip().split()
        print("\nRunning:", " ".join(cmd))
        subprocess.run(cmd)


print("LiftOCR PyTorch Installer")
print("--------------------------")

if has_nvidia_gpu():
    cuda_version = get_cuda_version()
    print("Detected NVIDIA GPU")
    print(f"CUDA Version: {cuda_version}")
    print("Recommended: PyTorch with CUDA", cuda_version)
else:
    cuda_version = None
    print("No NVIDIA GPU detected. Recommended: CPU-only install.")

print("\nOptions:")
print("1) Install Recommended CUDA Version")
print("2) Install CPU-only Version")
print("3) Enter Manual pip command")

choice = input("\nEnter choice (1/2/3): ").strip()
install_pytorch(choice, cuda_version)
