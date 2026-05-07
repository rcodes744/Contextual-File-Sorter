import os

def format_size(bytes_size):
    """Converts bytes to a human-readable string (MB)."""
    return f"{bytes_size / (1024 * 1024):.2f} MB"

def ensure_dir(path):
    """Creates a directory if it doesn't already exist."""
    if not os.path.exists(path):
        os.makedirs(path)