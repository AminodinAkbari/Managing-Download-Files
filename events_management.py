from watchdog.events import FileSystemEventHandler
from folder_management import FoldersControl
import os

class DownloadHandler(FileSystemEventHandler):
    """This class will listen to file system event , to whenever a file being downloaded , the script can use the other function of this code foe moving the files or any other future."""
    
    def __init__(self) -> None:
        """Define the paths with variables."""
        self.chrome_downloads_folder = FoldersControl.chrome_downloads_folder
        self.video_folder = FoldersControl.video_folder
        self.song_folder = FoldersControl.song_folder 
        self.image_folder = FoldersControl.image_folder
        self.browsers_zip_folder = FoldersControl.browsers_zip_folder
        self.other_folder = FoldersControl.other_folder
        self.zip_folder = FoldersControl.zip_folder
        
        self.telegram_downloads_folder = FoldersControl.telegram_downloads_folder
    
    def on_modified(self, event) -> None:
        """listen to file systems to check new files downloaded in 'Downloads' and 'Telegram' folder."""
        for filename in os.listdir(self.chrome_downloads_folder):
            file_path = os.path.join(self.chrome_downloads_folder, filename)
            if not os.path.isfile(file_path):
                continue

            print(f"Detected file: {file_path}")
            
            # Check if file is still being downloaded (skip temporary files)
            if filename.endswith('crdownload') or filename.endswith('.part'):
                continue  # Skip incomplete downloads
            
            extension_to_folder = {
                ('.mp4', '.mkv', '.avi'): self.video_folder,
                ('.mp3', '.wav'): self.song_folder,
                ('.jpg', '.jpeg', '.png', '.HEIC'): self.image_folder,
                ('.zip', '.rar', '.tar'): self.browsers_zip_folder,
            }

            # Move based on file type
            for extension , folder in extension_to_folder.items():
                if filename.endswith(extension):
                    print("it's a common")
                    FoldersControl.move_file(file_path , folder)
                else:
                    print("It's going to others")
                    # Other types of files will moved to 'other' folder path
                    FoldersControl.move_file(file_path , self.other_folder)

        # Telegram Downloads
        for filename in os.listdir(self.telegram_downloads_folder):
            file_path = os.path.join(self.telegram_downloads_folder, filename)
            if not os.path.isfile(file_path):
                continue
            
            if filename.endswith(('.zip', '.rar')):
                FoldersControl.move_file(file_path, self.zip_folder)