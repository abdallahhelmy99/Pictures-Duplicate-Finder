import os
import numpy as np
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

# Load the VGG16 model
model = VGG16(weights='imagenet', include_top=False)

# Function to calculate the feature vector of an image
def image_features(filepath):
    img = image.load_img(filepath, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    features = model.predict(img_data)
    return features.flatten()

# Create a root Tk window and hide it
root = tk.Tk()
root.withdraw()

# Ask the user to choose a folder
folder_path = filedialog.askdirectory()

# Dictionary to store image features
features = defaultdict(list)

print("Loading... This might take a while for large folders.")

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    # Skip directories and non-image files
    if os.path.isdir(filepath) or not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue
    # Calculate the feature vector of the image
    image_features_vector = image_features(filepath)
    # Add the filename to the list of files with the same features
    features[str(image_features_vector)].append(filepath)

duplicates_found = False

# Ask the user if they want to delete all duplicates
delete_all = input('Do you want to delete all duplicates without asking for each one? (y/n): ').lower() == 'y'

# Check for duplicate images and ask the user if they want to delete them
for feature_vector, filepaths in features.items():
    if len(filepaths) > 1:
        duplicates_found = True
        print(f'Duplicate images for feature vector {feature_vector}:')
        for filepath in filepaths:
            print(f'\t{filepath}')
        if delete_all or input('Do you want to delete these duplicates? (y/n): ').lower() == 'y':
            # Delete all but one of the duplicates
            for filepath in filepaths[1:]:
                os.remove(filepath)
                print(f'Deleted {filepath}')

if not duplicates_found:
    print("No duplicate images were found.")