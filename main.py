import os
from collections import defaultdict
import hashlib
import tkinter as tk
from tkinter import filedialog

# Function to calculate the hash of a file
def file_hash(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

# Create a root Tk window and hide it
root = tk.Tk()
root.withdraw()

# Ask the user to choose a folder
folder_path = filedialog.askdirectory()

# Dictionary to store file hashes
hashes = defaultdict(list)

print("Loading... This might take a while for large folders.")

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    # Skip directories
    if os.path.isdir(filepath):
        continue
    # Calculate the hash of the file
    file_hash_value = file_hash(filepath)
    # Add the filename to the list of files with the same hash
    hashes[file_hash_value].append(filepath)

duplicates_found = False

# Ask the user if they want to delete all duplicates
delete_all = input('Do you want to delete all duplicates without asking for each one? (y/n): ').lower() == 'y'

# Check for duplicate files and ask the user if they want to delete them
for hash_value, filepaths in hashes.items():
    if len(filepaths) > 1:
        duplicates_found = True
        print(f'Duplicate files for hash {hash_value}:')
        for filepath in filepaths:
            print(f'\t{filepath}')
        if delete_all or input('Do you want to delete these duplicates? (y/n): ').lower() == 'y':
            # Delete all but one of the duplicates
            for filepath in filepaths[1:]:
                os.remove(filepath)
                print(f'Deleted {filepath}')

if not duplicates_found:
    print("No duplicate files were found.")