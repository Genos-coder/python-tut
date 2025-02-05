# 🔄 **Auto-reload Python on File Changes** 🚀

This guide will help you automatically execute a Python file every time you make changes to it. It's useful for rapid development when you're frequently modifying scripts.

---

## 📋 **Steps to Set Up:**

### 1️⃣ **Create a Virtual Environment**

Run the following command to create a new virtual environment:

```bash
python -m venv venv
```

---

### 2️⃣ **Activate the Virtual Environment**

Activate the virtual environment. If you're using **VSCode**, it usually activates automatically when you open the project. Otherwise, run:

- **For Windows** (Command Prompt):

  ```bash
  .venv\Scripts\activate
  ```

- **For macOS/Linux** (Terminal):
  ```bash
  source venv/bin/activate
  ```

When the environment is active, your terminal prompt should look like this:

```bash
(venv) C:\your-project-directory>
```

---

### 3️⃣ **Deactivate the Virtual Environment**

When you're done working, you can deactivate the virtual environment by running:

```bash
deactivate
```

---

### 4️⃣ **Install `watchdog`**

To automatically monitor file changes, install `watchdog` in your virtual environment:

```bash
pip install watchdog
```

---

### 5️⃣ **Create `auto-reload.py`**

Create a file named `auto-reload.py` in your current working directory. Add the following code to it.

Make sure to replace `"your_script.py"` with the name of the Python script you want to run.

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):  # Check if the modified file is a Python file
            print(f"🚨 Detected change in {event.src_path}. Restarting script... 🔄")
            subprocess.run(["python", "your_script.py"])  # Replace "your_script.py" with your file name

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
```

---

### ⚡ **How It Works:**

- The script will watch for any changes in `.py` files.
- When a change is detected, it will automatically restart the specified Python script (in this case, `"your_script.py"`).
- This is helpful for rapid development and testing without needing to manually restart your scripts!

---

### 🎯 **Test It Out:**

1. Make sure you're in the correct directory and have the correct Python script set.
2. Run `auto-reload.py` by executing:

```bash
python auto-reload.py
```

3. Now, every time you modify and save your Python file (e.g., `your_script.py`), it will automatically restart the script! ⚡

---

Let me know if you need any further adjustments or help! 😊
