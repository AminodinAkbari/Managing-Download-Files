import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from dotenv import load_dotenv
load_dotenv() 

personal_folder_name_in_home_dir = os.getenv("PersonalFolderName")

if not personal_folder_name_in_home_dir:
    # TODO: Write a better message and make the user understand
    raise Exception("Error . you not write your folder name in .env file")

# Define the source folders for Chrome and Telegram
chrome_downloads_folder = '/home/amin/Downloads'
telegram_downloads_folder = '/home/amin/Downloads/Telegram Desktop'

# Define the destination folders
video_folder = '/home/amin/Downloads/videos'
song_folder = '/home/amin/Downloads/songs'
image_folder = '/home/amin/Downloads/images'
browsers_zip_folder = '/home/amin/Downloads/browser_zips'
zip_folder = '/home/amin/Downloads/zips'
other_folder = '/home/amin/Downloads/others'

# Ensure folders exist or create them
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, mode=0o777, exist_ok=True)

# Move file to the destination folder
def move_file(file_path, destination_folder):
    create_folder_if_not_exists(destination_folder)  # Ensure destination folder exists
    print(f"Moving {file_path} to {destination_folder}")
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Chrome Downloads
        for filename in os.listdir(chrome_downloads_folder):
            file_path = os.path.join(chrome_downloads_folder, filename)
            if not os.path.isfile(file_path):
                continue

            print(f"Detected file: {file_path}")
            
            # Check if file is still being downloaded (skip temporary files)
            if filename.endswith('.crdownload') or filename.endswith('.part'):
                continue  # Skip incomplete downloads

            # Move based on file type
            if filename.endswith(('.mp4', '.mkv', '.avi')):
                move_file(file_path, video_folder)
            elif filename.endswith(('.mp3', '.wav')):
                move_file(file_path, song_folder)
            elif filename.endswith(('.jpg', '.jpeg', '.png', '.HEIC')):
                move_file(file_path, image_folder)
            elif filename.endswith(('.zip', '.rar', '.tar')):
                move_file(file_path, browsers_zip_folder)
            else:
                move_file(file_path, other_folder)

        # Telegram Downloads
        # for filename in os.listdir(telegram_downloads_folder):
        #     file_path = os.path.join(telegram_downloads_folder, filename)
        #     if not os.path.isfile(file_path):
        #         continue
            
        #     if filename.endswith(('.zip', '.rar')):
        #         move_file(file_path, zip_folder)

# Function to start monitoring the folders
def monitor_folders():
    print("Start monitoring")
    event_handler = DownloadHandler()
    observer = Observer()

    # Observe Chrome downloads folder
    observer.schedule(event_handler, chrome_downloads_folder, recursive=False)
    
    # Observe Telegram downloads folder
    # observer.schedule(event_handler, telegram_downloads_folder, recursive=False)

    observer.start()
    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_folders()
