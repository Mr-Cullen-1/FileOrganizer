# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:50:29 2024

@author: Jacob Cullen

File organizer
"""

import os
import shutil

def organize_files(folder_path):
    # Dictionary to hold file extensions and their corresponding directories
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Audios": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar.gz"],
        "Executables": [".exe", ".msi"],
        "Others": []  # For any other file types
    }

    # Create directories if they don't exist
    for directory in extensions.keys():
        directory_path = os.path.join(folder_path, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    # Organize files
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            # Get file extension
            _, extension = os.path.splitext(file)
            extension = extension.lower()

            # Find the appropriate directory for the file
            for category, extension_list in extensions.items():
                if extension in extension_list:
                    destination_folder = os.path.join(folder_path, category)
                    shutil.move(os.path.join(folder_path, file), destination_folder)
                    break
            else:
                # If no category found, move to "Others" directory
                destination_folder = os.path.join(folder_path, "Others")
                shutil.move(os.path.join(folder_path, file), destination_folder)

    print("Files have been organized successfully!")

# Example usage
if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder to organize: ")
    organize_files(folder_to_organize)
