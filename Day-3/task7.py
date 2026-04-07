import os
import time
from datetime import datetime
 
WATCH_DIR = r"C:\Users\9901363\Desktop\Trainer Classes\Day-3"
LOG_FILE = "app.log"
 
 
def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
 
def get_timestamp():
    return datetime.now().strftime("%d-%b-%Y %H:%M")
 
def watch_directory(path):
    prev_files = set(os.listdir(path))
 
    while True:
        time.sleep(2)
        curr_files = set(os.listdir(path))

        created = curr_files - prev_files
        for file in created:
            msg = f"{get_timestamp()}  file named {file} [CREATED]"
            print(msg)
            log_event(msg)

        deleted = prev_files - curr_files
        for file in deleted:
            msg = f"{get_timestamp()}  file named {file} [DELETED]"
            print(msg)
            log_event(msg)
        prev_files = curr_files
 
 
if __name__ == "__main__":
    print(f"Watching directory: {WATCH_DIR}")
    watch_directory(WATCH_DIR)