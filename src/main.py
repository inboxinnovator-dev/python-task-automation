import os
import shutil
import logging
import re
from datetime import datetime

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- DIRECTORIES ----------------
SOURCE_DIR = "data/sample_files"
DEST_DIR = "output/organized_files"

# ---------------- REGEX PATTERN ----------------
FILE_PATTERN = r"report_\d{4}-\d{2}-\d{2}\.\w+"

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created folder: {path}")

def organize_files():
    try:
        create_folder(DEST_DIR)

        for file in os.listdir(SOURCE_DIR):
            file_path = os.path.join(SOURCE_DIR, file)

            if os.path.isfile(file_path):

                # 👉 REGEX CHECK ADDED HERE
                if not re.match(FILE_PATTERN, file):
                    logging.info(f"Skipped file (pattern mismatch): {file}")
                    continue

                # Extract file extension
                ext = file.split(".")[-1]
                ext_folder = os.path.join(DEST_DIR, ext)
                create_folder(ext_folder)

                # Add timestamp to filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_name = f"{timestamp}_{file}"

        
                shutil.move(file_path, os.path.join(ext_folder, new_name))
                logging.info(f"Moved file: {file} → {new_name}")

        print("Files organized successfully")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        print("Error occurred. Check logs.")

# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    organize_files()


