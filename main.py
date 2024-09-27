from events_management import DownloadHandler
from watchdog.observers import Observer
import time

# Function to start monitoring the folders
def monitor_folders():
    print("Start monitoring")
    event_handler = DownloadHandler()
    observer = Observer()

    # Observe Chrome downloads folder
    observer.schedule(event_handler, event_handler.chrome_downloads_folder, recursive=False)
    
    # Observe Telegram downloads folder
    observer.schedule(event_handler, event_handler.telegram_downloads_folder, recursive=False)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping folder monitor...")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_folders()