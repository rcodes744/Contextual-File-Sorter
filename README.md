# Contextual File Sorter
**Author:** Riya

## 🚀 Overview
This project is a local automation tool designed to fix "Download folder clutter." Unlike standard sorters, this uses Python's `os` and `datetime` modules to sort files based on:
* **Size:** Files over 100MB are sent to a 'Large Files' archive.
* **Date:** Regular files are organized into 'Month_Year' folders based on when they were created.

## 🏗️ Architecture
- `main.py`: The engine that runs the sorting loop.
- `sorter_logic.py`: The brain that analyzes file metadata.
- `config.py`: User settings for file paths.
- `utils.py`: Helper functions for formatting and folder creation.
