import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trial.ipynb"
]

for file in files:
    file = Path(file)
    file_dir, file_name = os.path.split(file)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory; {file_dir} for the file: {file_name}")

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, "w") as f:
            pass
            logging.info(f"Creating empty file: {file}")
    else:
        logging.info(f"{file_name} is already exists")
