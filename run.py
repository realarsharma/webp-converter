import sys
import subprocess
from pathlib import Path

# Path to venv
VENV_PATH = Path(__file__).parent / "webp-converter-env"
SCRIPT_PATH = Path(__file__).absolute()

# Auto-activate venv if not already running inside it
if sys.prefix != str(VENV_PATH):
    python_exe = VENV_PATH / "Scripts" / "python.exe"
    if not python_exe.exists():
        print("⚠️ Virtual environment not found! Please run:")
        print("python -m venv webp-converter-env")
        print("pip install -r requirements.txt")
        sys.exit(1)
    subprocess.run([str(python_exe), str(SCRIPT_PATH)])
    sys.exit()

# Import main logic after venv is activated
from main import optimize_images_folder
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# ----------------------------
# User-configurable settings
# ----------------------------
MAX_DIMENSION = 1000   # Max width or height
QUALITY = 80           # WebP quality (0-100)
CONVERT_WEBP = True    # Convert all images to WebP?

SRC_FOLDER = PROJECT_ROOT / "Org-Image"
DST_FOLDER = PROJECT_ROOT / "Opt-Image"

# Run optimizer
optimize_images_folder(SRC_FOLDER, DST_FOLDER, max_dimension=MAX_DIMENSION, quality=QUALITY, convert_webp=CONVERT_WEBP)
