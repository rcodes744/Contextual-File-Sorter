#This is the "Brain" of the operation. It decides where files go based on the context.


import os
from datetime import datetime
import config

def get_destination_path(file_path):
    """
    Analyzes file metadata to determine the target subfolder.
    Returns the path with the format: Year-Month (e.g., 2026-May)
    """
    # 1. Size Check
    file_size = os.path.getsize(file_path)
    if file_size > config.BIG_FILE_THRESHOLD:
        return os.path.join(config.DEST_BASE, "Large_Media_Archive")

    # 2. Time Check
    # We use getmtime (modification time) or getctime (creation time)
    timestamp = os.path.getmtime(file_path)
    date_obj = datetime.fromtimestamp(timestamp)
    
    # Riya's Custom Format: "2026-May"
    # %Y = Year, %B = Full Month name (e.g., January, May)
    folder_name = date_obj.strftime("%Y-%B") 
    
    return os.path.join(config.DEST_BASE, folder_name)