# Project: Contextual File Sorter
# Author: Riya

import os

# Update these paths to your actual local directories
SOURCE_DIR = r"C:\Users\Riya Thakkar\Downloads" 
DEST_BASE = r"C:\Users\Riya Thakkar\Documents\Riya_Sorted_Vault"

# Metadata Thresholds
# 100MB threshold (100 * 1024 * 1024 bytes)
BIG_FILE_THRESHOLD = 100 * 1024 * 1024