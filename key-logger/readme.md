
# 📝 Keylogger with Screenshot Capture

This is a Python-based keylogger that logs keystrokes and captures screenshots when the **Enter** key is pressed. All keypresses are logged with timestamps, and the logs are saved to a text file. Additionally, screenshots are saved in a dedicated folder whenever the **Enter** key is pressed.

## 🚀 Features:
- **⌨️ Key Logging**: Logs each keypress along with a timestamp. Special keys are labeled with human-readable text.
- **📸 Screenshot Capture**: Automatically takes a screenshot when the **Enter** key is pressed.
- **🗂️ Organized File Structure**: Logs are saved in `key_log.txt`, and screenshots are stored in a `screenshots/` folder.

## 📂 Project Structure:
```
.
├── key_log.txt               # File containing the keypress logs with timestamps
├── screenshots/              # Folder where screenshots are stored
│   └── screen_<timestamp>.png  # Screenshot image files
└── key-logger.py                      # Main Python script
```

### Example of Log Entry in `key_log.txt`:
```
[2025-04-21 14:30:15]: a
[2025-04-21 14:30:17]: b
[2025-04-21 14:30:18]: [SPACE]
[2025-04-21 14:30:19]: [SHIFT]
[2025-04-21 14:30:21]: [ENTER]
```

Each log entry contains:
- The timestamp of when the key was pressed.
- The key that was pressed (e.g., `a`, `b`, `[SPACE]`, `[SHIFT]`).

```

## 🛠️ Requirements:
- Python 3.x
- Required Python libraries:
  - `pynput` (for key logging)
  - `pyautogui` (for screenshot capture)

### Installing the Required Libraries:
Run the following commands to install the necessary libraries:

```bash
pip install pynput pyautogui
```

## 🏃‍♂️ How to Run:
1. Clone or download this project.
2. Open a terminal/command prompt.
3. Navigate to the project directory.
4. Run the `key-logger.py` script using Python:

```bash
python key-logger.py
```

## ⚠️ Important Notes:
- **Permissions**: Please ensure that you have explicit permission to use this tool on the system, as logging keystrokes without consent may be illegal.
- **Use Case**: This keylogger is intended for educational purposes only. Do not use it for any illegal activities.

## 📜 Disclaimer:
This tool is for educational purposes and should be used responsibly. Unauthorized use of keyloggers is illegal in many jurisdictions. Always follow the laws in your area when using such tools.

## 📧 Future Enhancements (Planned for Development):
1. **🔒 Encryption**: Encrypt key logs before saving them to ensure privacy.
2. **📧 Email Logging**: Automatically email the logs and screenshots to a predefined email address.
3. **🔄 Persistent Background Mode**: Keep the keylogger running in the background even after rebooting the system.
4. **🔥 Start/Stop Hotkey**: Add functionality to start and stop the keylogger using a hotkey combination.
5. **⚖️ Log File Size Limit**: Automatically archive logs when they reach a certain size.
6. **🖥️ Multithreading for Efficiency**: Run key logging and screenshot capture in separate threads for better performance.
7. **🌐 Remote Access**: Provide access to the logs and screenshots remotely through a web interface or cloud storage.

