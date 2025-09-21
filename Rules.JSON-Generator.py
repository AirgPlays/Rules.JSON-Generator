"""
===========================================================
              Generate rules.json 
===========================================================

This script downloads a hosts file from a GitHub raw link
and generates a rules.json.

Each rule:
- Starts with user-defined starting ID (default = 1)
- Has user-defined priority (default = 1)
- No redirect link by default

Warning: Currently only works with GitHub raw links.

Author: AirgPlays
Copyright: 9/21/25
License: Creative Commons Zero v1.0 Universal
===========================================================
"""

import requests
import json
import tkinter as tk
from tkinter import messagebox, filedialog

def generate_rules():
    url = entry_url.get().strip()
    if not url.startswith("https://raw.githubusercontent.com/"):
        messagebox.showwarning("Warning", "Currently only works for GitHub raw links!")
        return

    # Get starting ID and priority, use defaults if blank
    try:
        start_id = int(entry_id.get().strip() or 1)
        priority = int(entry_priority.get().strip() or 1)
    except ValueError:
        messagebox.showerror("Error", "Starting ID and Priority must be integers!")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download file:\n{e}")
        return

    lines = response.text.splitlines()
    rules = []
    current_id = start_id

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or "localhost" in line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        domain = parts[1]
        rules.append({
            "id": current_id,
            "priority": priority,
            "condition": { "urlFilter": f"*://{domain}/*" }
        })
        current_id += 1

    # Ask user where to save
    save_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")],
        initialfile="rules.json",
        title="Select download location to save rules.json"
    )
    if save_path:
        with open(save_path, "w") as f:
            json.dump(rules, f, indent=4)
        messagebox.showinfo(
            "Success",
            f"rules.json created with {len(rules)} entries!\nSaved to:\n{save_path}"
        )

# Create GUI
root = tk.Tk()
root.title("Rules.json Generator")

tk.Label(root, text="Enter GitHub raw hosts file link:").pack(padx=10, pady=(10,0))
entry_url = tk.Entry(root, width=80)
entry_url.pack(padx=10, pady=5)

tk.Label(root, text="Starting ID (enter = default 1):").pack(padx=10, pady=(10,0))
entry_id = tk.Entry(root, width=20)
entry_id.pack(padx=10, pady=5)

tk.Label(root, text="Priority (enter = default 1):").pack(padx=10, pady=(10,0))
entry_priority = tk.Entry(root, width=20)
entry_priority.pack(padx=10, pady=5)

tk.Button(root, text="Generate rules.json", command=generate_rules).pack(padx=10, pady=20)

root.mainloop()
