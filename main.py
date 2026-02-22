import pyautogui
import time
import sys
import os
import threading
import tkinter as tk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

IMAGE_NAME = resource_path("skip_button.png")
running = False  # Track if the skipper is ON or OFF

def skipper_logic():
    """Background loop that looks for ads only when 'running' is True"""
    global running
    while True:
        if running:
            try:
                button = pyautogui.locateOnScreen(IMAGE_NAME, confidence=0.7, grayscale=True)
                if button:
                    pyautogui.click(pyautogui.center(button))
                    time.sleep(2)
            except:
                pass
        time.sleep(1)

def toggle():
    """Toggles the state and updates button color/text"""
    global running
    running = not running
    if running:
        btn.config(text="SKIPPER: ON", bg="#2ecc71", fg="white")
    else:
        btn.config(text="SKIPPER: OFF", bg="#e74c3c", fg="white")

# --- UI Setup ---
root = tk.Tk()
root.title("YT Skip")
root.geometry("150x60")
root.attributes("-topmost", True) # Keeps the button on top of your browser

btn = tk.Button(root, text="SKIPPER: OFF", bg="#e74c3c", fg="white", 
                font=("Arial", 10, "bold"), command=toggle)
btn.pack(expand=True, fill="both")

# Start the logic in a separate thread so the window doesn't freeze
threading.Thread(target=skipper_logic, daemon=True).start()

root.mainloop()