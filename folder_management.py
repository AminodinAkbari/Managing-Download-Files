import os
import shutil
from dotenv import load_dotenv
load_dotenv()

class FoldersControl:
    # Define the source folders for Chrome and Telegram
    home_dir = os.getenv("HOME")  # Default to '/home/amin' if $HOME isn't set
    if not home_dir:
        raise Exception("PersonalFolderName not found in .env file. Please set it before running the script.")
    
    print("THIS IS home_dir : " , home_dir)
    chrome_downloads_folder = f"{home_dir}/Downloads"
    telegram_downloads_folder = f'{home_dir}/Downloads/Telegram Desktop'

    # Define the destination folders
    video_folder = f'{home_dir}/Downloads/videos'
    song_folder = f'{home_dir}/Downloads/songs'
    image_folder = f'{home_dir}/Downloads/images'
    browsers_zip_folder = f'{home_dir}/Downloads/browser_zips'
    zip_folder = f'{home_dir}/Downloads/zips'
    other_folder = f'{home_dir}/Downloads/others'
    
    print("______________________")
    print(chrome_downloads_folder)
    print(telegram_downloads_folder)
    print("______________________")
    
    print(video_folder)
    print(song_folder)
    print(image_folder)
    print(browsers_zip_folder)
    print(browsers_zip_folder)
    print(zip_folder)
    print(other_folder)
        
    @classmethod
    def create_folder_if_not_exists(cls , folder_path) -> None:
        """
        Check if "folder_path" is a real path or not. this function will create a folder if that "folder_path" not exists, if "folder_path" already exists in system , it will do nothing (The 'exist_ok' will do it)
        """
        if not os.path.exists(folder_path):
            print("CODE CERATE NEW DIRECTORY : " , folder_path)
            os.makedirs(folder_path , mode=0o777 , exist_ok=True)
            
    @classmethod
    def move_file(cls, current_file_path: str, destination_folder_path: str) -> None:
        """Move downloaded file using 'move' function."""
        # Check if the file is still downloading or is a temporary/hidden file
        if current_file_path.endswith('crdownload') or current_file_path.startswith('.'):
            print(f"Skipping file: {current_file_path}")
            return

        # Double-check if the file still exists before trying to move it
        if not os.path.exists(current_file_path):
            print(f"File not found: {current_file_path}, skipping move.")
            return

        # Check if destination folder exists, if not, create it
        cls.create_folder_if_not_exists(destination_folder_path)
        print(f" === Moving {current_file_path} to {destination_folder_path} ===")
        
        try:
            shutil.move(current_file_path, os.path.join(destination_folder_path, os.path.basename(current_file_path)))
        except FileNotFoundError as e:
            print(f"Error moving file: {current_file_path} -> {e}")
        # What is that "basename" above line ? it will select the file name. then the "join" from "os" will combine the destination path and current_file_path via '/' if it's needed. with this , the "move" function know where should the file will be move.