# Pictures Duplicate Finder and Remover

This Python script helps you find and remove duplicate files in a selected directory. It uses MD5 hashing to identify duplicate files.

## How it works

1. The script first asks the user to select a directory.
2. It then iterates over all files in the directory, skipping subdirectories.
3. For each file, it calculates an MD5 hash.
4. It stores each file's path in a dictionary, using the file's hash as the key.
5. After all files have been processed, it checks the dictionary for any hashes that have more than one associated file path. These are the duplicate files.
6. The user is then asked if they want to delete all duplicates without confirmation for each one. If they choose 'yes', all duplicates are deleted. If they choose 'no', they will be asked for confirmation for each set of duplicates.
7. If no duplicates are found, a message is printed to the console.

## Requirements

- Python 3
- tkinter module for Python 3

## Usage

Run the script in a Python 3 environment. When prompted, select the directory you want to check for duplicate files.

```bash
python main.py
```

## Note

This script only checks for duplicates in the selected directory, not in its subdirectories. It also does not handle file read errors or other exceptions that might occur during file processing.
