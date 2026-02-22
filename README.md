# 🎥 YouTube Ad-Skipper (Automation Tool)

A lightweight Python automation tool that utilizes **Computer Vision** to detect and automatically click the "Skip Ad" button on YouTube. It features a simple ON/OFF toggle interface that stays on top of your browser for easy access.



## ✨ Features
* **Automated Detection:** Uses template matching to "see" the Skip Ad button.
* **UI Toggle:** A small, "always-on-top" window to enable or disable the skipper.
* **Multi-Threaded:** The UI and detection logic run on separate threads to prevent lag.
* **Safe-Exit:** Built-in fail-safe (move mouse to top-left corner) to kill the process instantly.

## 🛠️ How it Works (Technical Details)
This project is a practical application of **Pattern Matching** and **Asynchronous Programming**.

### Algorithm Complexity
The script uses `pyautogui.locateOnScreen()`, which performs a sliding window search across the screen pixels.
* **Search Complexity:** Approximately $O(W \times H \times w \times h)$, where $(W,H)$ is screen resolution and $(w,h)$ is the button size.
* **Optimization:** Grayscale conversion is enabled to reduce processing load by **66%** (moving from 3 color channels to 1).

### Threading Architecture
To provide a smooth **UI/UX**, the program uses:
* **Main Thread:** Handles the Tkinter event loop for the button interface.
* **Daemon Thread:** Runs the infinite search loop for ad detection, ensuring the GUI remains responsive.

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+
* Your own screenshot of the "Skip Ad" button (saved as `skip_button.png`).

### 2. Installation
Clone the repository and install the dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/Youtube-Ad-Skipper.git](https://github.com/YOUR_USERNAME/Youtube-Ad-Skipper.git)
cd Youtube-Ad-Skipper
pip install -r requirements.txt

Run the script directly:
python main.py
Or use the compiled .exe version from the dist folder.

⚠️ Important Precautions
Antivirus: Since this script controls the mouse, software like Avast may flag it. You must add the project folder to your Antivirus Exclusions/Exceptions list.

Screen Resolution: The skip_button.png must be captured on the same monitor and resolution where you watch YouTube.

👨‍💻 Author
Koviri kalyan jagan kumar

Current Project: YouTube Automation & DSA 75-Day Challenge.

Also check out my other project: [suseme-chat-app]
