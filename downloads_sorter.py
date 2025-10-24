#!/usr/bin/env python3
# downloads_sorter.py
# This script sorts the contents of the user's system Downloads folder into in the correct folder
# Written by: JakeTheSnake(JMG3000)

import os
import shutil

# Define the path to the downloads folder
DOWNLOADS_PATH = os.path.expanduser('~\Downloads')

# Define the categories and their corresponding file extensions
# Review the file types before executing
CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xlsm", ".xls", ".pptx", ".ppt"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".m4v", ".rm", ".rmvb"],
    "Music": [".wav", ".mp3", ".aac", ".flak"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".bz", ".xz", ".7z"],
    "Executables": [".exe", ".dmg", ".msi", ".lnk"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php"],

}

#function to apply the CATEGORIES extension values to found file types
def categorize_fil(filename):
    try:
        ext = os.path.splitext(filename)[1].lower()
        for category, extensions in CATEGORIES.items():
            if ext in extensions:
                return category
        return "Other"

    except Exception as e:
        print(f"Failed to access directory or file {filename}.  Error Code{e}")

def organize_downloads():

    #for each item found in the folder/directory
    for item in os.listdir(DOWNLOADS_PATH):

        #concatenates a unique string using .join using the existing
        #directory and each file inside
        item_path = os.path.join(DOWNLOADS_PATH, item)

        #check if there
        if os.path.isfile(item_path):
            category = categorize_fil(item)
            target_folder = os.path.join(DOWNLOADS_PATH, category)
            os.makedirs(target_folder, exist_ok=True)
            target_path = os.path.join(target_folder, item)

           # attempt to move a file to the desired location
            try:
                shutil.move(item_path, target_path)
                print("Moving {} to {}".format(item_path, target_path))

                # attempt to delete the file after coping is successful
                try:
                    os.remove(item_path)
                    print("Removing {}".format(item_path))

                # catch an exception when the original file is not removed
                except Exception as e:
                    print(f"Failed to remove {item_path}. Error Code{e}")

           # try an exception when the file is not moved
            except Exception as e:
                print(f"Failed to move {item_path} to {target_path}.  Error Code{e}")



if __name__ == "__main__":
    organize_downloads()
    print("...Done")
    print("The download folder in {}'s has been organized!".format(os.path.expanduser('~')))
    # I used the os.path.expanduser() method instead of os.getlogin() for reliability even in edge cases
