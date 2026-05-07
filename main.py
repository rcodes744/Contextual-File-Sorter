#The "Engine" that connects everything and executes the move.

# Purpose: Entry point for the automation tool

import os
import shutil
import time
import config
import sorter_logic
import utils

def start_sorting():
    print(f"--- Riya's File Sorter Active ---")
    print(f"Monitoring: {config.SOURCE_DIR}")

    # Ensure the base destination exists using our utility
    utils.ensure_dir(config.DEST_BASE)

    # listdir scans the folder for all items
    files_processed = 0
    for filename in os.listdir(config.SOURCE_DIR):
        file_path = os.path.join(config.SOURCE_DIR, filename)

        # We only want to move files, not other folders
        if os.path.isfile(file_path):
            try:
                # Get the 'Contextual' destination
                target_folder = sorter_logic.get_destination_path(file_path)
                utils.ensure_dir(target_folder)

                # Execute the move
                shutil.move(file_path, os.path.join(target_folder, filename))
                
                size_readable = utils.format_size(os.path.getsize(os.path.join(target_folder, filename)))
                print(f"✅ Moved {filename} ({size_readable})")
                files_processed += 1
                
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")

    print(f"--- Task Complete. Files Organized: {files_processed} ---")

if __name__ == "__main__":
    start_sorting()