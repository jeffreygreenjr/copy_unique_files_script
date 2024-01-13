import os
import shutil

def copy_unique_files(source_folder, destination_folder):

    # Get the list of files in source and destination folders
    source_files = set(os.listdir(source_folder))
    destination_files = set(os.listdir(destination_folder))

    # Identify new files (files in source but not in destination)
    new_files = source_files - destination_files

    # Copy new files from source to destination
    for file_name in new_files:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {file_name}")
        

