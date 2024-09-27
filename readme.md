# Folder Management and File Organizer

This project is designed to automatically organize files downloaded via Chrome and Telegram. The script monitors specified download folders and moves files based on their type to appropriate destination folders.

## Features

- Automatically monitors Chrome (or any other browser) and Telegram download folders.
- Moves files into categorized folders like videos, images, songs, and more.
- Flexible folder creation if the destination folder does not exist.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- `watchdog` package
- `python-dotenv` package
- `shutil` (comes pre-installed with Python)

You can install required packages via:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the Repository** :

   ```
   git clone <your-repo-url>
   cd folder-management
   ```

 **Set Up Environment Variables** :

* Create a `.env` file in the root directory.
* Add the following environment variables to specify your personal folder in your home directory:

```bash
HOME= 'your home directory , like /home/username' 
```

If you set this address wrong , the script will crashed.

 **Project Structure** :
├── folder_management.py       # Handles the folder operations like creating folders and moving files
├── events_management.py       # Listens for file system events and triggers file moves
├── main.py                    # The entry point that starts the folder monitoring
└── .env                       # Environment variables (PersonalFolderName)

## How to Run

1. **Monitor Folders** :
   Run the script using the following command:

```bash
python3 main.py
```

   This will start monitoring your Chrome and Telegram download folders for new files and automatically move them to the appropriate destination folders.

1. **File Movement** :

* Videos (e.g., `.mp4`, `.mkv`) are moved to the `Downloads/videos` folder.
* Songs (e.g., `.mp3`, `.wav`) are moved to the `Downloads/songs` folder.
* Images (e.g., `.jpg`, `.png`) are moved to the `Downloads/images` folder.
* Zip files (e.g., `.zip`, `.rar`) are moved to the `Downloads/browser_zips` or `Downloads/zips` folder.
* Other files are moved to the `Downloads/others` folder.

## Customization

If you need to monitor different folders or move different types of files, you can modify the paths and file types in `DownloadHandler` class located in `events_management.py`.


## Future Plans

1. **Dockerize the project** : Make the project containerized to ease deployment and setup.
2. **Cross-platform compatibility** : Allow the project to run on Windows without requiring users to set the home directory manually.
3. **Handling large files differently** : Instead of moving large files (above 250 MB), the script will create a folder with the same name as the file and move the file into it.
4. **Optimization** : Improve the performance of the script, especially when handling multiple large file downloads at once.


## Contributions

Feel free to fork the project, create issues, or submit pull requests if you'd like to contribute.
