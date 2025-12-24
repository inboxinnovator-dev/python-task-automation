import os
import shutil
import logging
from datetime import datetime

logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

SOURCE_DIR = "data/sample_files"
DEST_DIR = "output/organized_files"

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def organize_files():
    try:
        create_folder(DEST_DIR)

        for file in os.listdir(SOURCE_DIR):
            file_path = os.path.join(SOURCE_DIR, file)

            if os.path.isfile(file_path):
                ext = file.split('.')[-1]
                ext_folder = os.path.join(DEST_DIR, ext)
                create_folder(ext_folder)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_name = f"{timestamp}_{file}"

                shutil.move(file_path, os.path.join(ext_folder, new_name))
                logging.info(f"Moved {file}")

        print("Files organized successfully")

    except Exception as e:
        logging.error(str(e))
        print("Error occurred")

if __name__ == "__main__":
    organize_files()

