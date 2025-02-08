from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):  # Check if the modified file is a Python file
            print(f"Detected change in {event.src_path}. Restarting script...")
            subprocess.run(["python", "05_boolean.py"])

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
