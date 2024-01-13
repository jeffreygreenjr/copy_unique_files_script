import os
import shutil

def copy_unique_files(source_folder, destination_folder):

    # Get the list of files in source and destination folders
    source_files = set(os.listdir(source_folder))
    destination_files = set(os.listdir(destination_folder))

    new_files = source_files - destination_files
    