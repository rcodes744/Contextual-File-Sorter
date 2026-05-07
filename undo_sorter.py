# Project: File Sorter Undo Tool
# Author: Riya

import os
import shutil
import config

def undo_sorting():
    print(f"--- Riya's Undo Tool: Moving files back to {config.SOURCE_DIR} ---")
    
    if not os.path.exists(config.DEST_BASE):
        print("The sorted vault folder doesn't exist. Nothing to undo!")
        return

    # Look at every folder inside the Sorted Vault
    for foldername in os.listdir(config.DEST_BASE):
        folder_path = os.path.join(config.DEST_BASE, foldername)

        # Make sure it's a directory
        if os.path.isdir(folder_path):
            files_in_folder = os.listdir(folder_path)
            
            for filename in files_in_folder:
                current_file_path = os.path.join(folder_path, filename)
                original_destination = os.path.join(config.SOURCE_DIR, filename)

                try:
                    # Move file back to Downloads
                    shutil.move(current_file_path, original_destination)
                    print(f"Restored: {filename}")
                except Exception as e:
                    print(f"Could not restore {filename}: {e}")

            # Once all files are moved out, delete the empty folder
            try:
                os.rmdir(folder_path)
                print(f"🗑️ Deleted empty folder: {foldername}")
            except Exception as e:
                print(f"Could not delete folder {foldername}: {e}")

    print("\n--- Restore Complete! Your Downloads folder is back to normal. ---")

if __name__ == "__main__":
    undo_sorting()