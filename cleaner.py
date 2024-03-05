import os
import sys
import shutil
from rich.console import Console

C = Console()
folder_to_clean = "/Users/lucas/Downloads"
others_folder = f"{folder_to_clean}/autres"

folder_extensions = {
    ".pdf": f"{folder_to_clean}/pdf",
    ".docx": f"{folder_to_clean}/documents",
    ".pptx": f"{folder_to_clean}/documents",
    ".xlsx": f"{folder_to_clean}/documents",
    ".odt": f"{folder_to_clean}/documents",
    ".csv": f"{folder_to_clean}/documents",
    ".jpg": f"{folder_to_clean}/images",
    ".png": f"{folder_to_clean}/images",
    ".webp": f"{folder_to_clean}/images",
    ".jpeg": f"{folder_to_clean}/images",
    ".HEIC": f"{folder_to_clean}/images",
    ".mp3": f"{folder_to_clean}/musique",
    ".wav": f"{folder_to_clean}/musique",
    ".mp4": f"{folder_to_clean}/vidéos",
    ".avi": f"{folder_to_clean}/vidéos",
    ".py": f"{folder_to_clean}/programmes",
    ".c": f"{folder_to_clean}/programmes",
    ".sh": f"{folder_to_clean}/programmes",
    ".ipynb": f"{folder_to_clean}/programmes",
    ".zip": f"{folder_to_clean}/archives",
    ".tgz": f"{folder_to_clean}/archives",
    ".tar.xz": f"{folder_to_clean}/archives",
    ".app": f"{folder_to_clean}/applications",
    ".dmg": f"{folder_to_clean}/applications",
    "icns" : f"{folder_to_clean}/images",
    "ics" : f"{folder_to_clean}/images",
    "php" : f"{folder_to_clean}/programmes",
    "css" : f"{folder_to_clean}/programmes",
    "java" : f"{folder_to_clean}/programmes"
    }

with C.status("Parsing directory..."):
    folders = ['applications','archives','documents','programmes','musique','vidéos','images','pdf','autres','gros fichiers']
    files_moved = []

    big_files_folder = f"{folder_to_clean}/gros fichiers"
    nb_files_moved = 0
    three_hundred_mb = 1073741824 / 3

    for file in os.listdir(folder_to_clean):
        extension = os.path.splitext(file)[1]
        if os.path.getsize(f"{folder_to_clean}/{file}") > three_hundred_mb:
            dest_folder = big_files_folder
            do_sth = True
        elif extension in folder_extensions:
            dest_folder = folder_extensions[extension]
            do_sth = True
        elif file in folders:
            do_sth = False
        else: 
            dest_folder = others_folder
            do_sth = True
        if do_sth:
            path_file = os.path.join(folder_to_clean, file)
            path_dest = os.path.join(dest_folder, file)
            shutil.move(path_file, path_dest)
            nb_files_moved += 1
            files_moved.append((file,dest_folder))
        
    C.log(f"{nb_files_moved} files moved")

