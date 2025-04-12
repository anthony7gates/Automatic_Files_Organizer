
import os
import shutil
import collections
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to organize the selected folder
def organize_folder():
    folder_path = filedialog.askdirectory(title="Select a Folder to Organize")
    if not folder_path:
        return

    file_mappings = collections.defaultdict(list)

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip hidden items
        if item.startswith('.'):
            continue

        # Determine file type or folder
        if os.path.isdir(item_path):
            ext = 'folders_misc'
        elif os.path.isfile(item_path):
            ext = item.split('.')[-1] if '.' in item else 'no_extension_files'
        else:
            ext = 'unknown'

        file_mappings[ext].append(item)

    for item_type, items in file_mappings.items():
        dest_folder = os.path.join(folder_path, item_type)
        os.makedirs(dest_folder, exist_ok=True)

        for item in items:
            src = os.path.join(folder_path, item)
            dest = os.path.join(dest_folder, item)
            try:
                if not os.path.exists(dest):
                    shutil.move(src, dest)
            except Exception as e:
                print(f"Error moving {item}: {e}")

    messagebox.showinfo("Done", f"Folder organized:\n{folder_path}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Folder Organizer")
root.geometry("350x180")
root.resizable(False, False)

label = tk.Label(root, text="Click the button to select and organize any folder by file type:", font=("Segoe UI", 10), pady=10)
label.pack()

button = tk.Button(root, text="Choose Folder & Organize", font=("Segoe UI", 12), bg="#2196F3", fg="white", padx=10, pady=5, command=organize_folder)
button.pack(pady=10)

root.mainloop()
