
# DevOps Python Automation 🚀

Welcome to my Python automation repository! This project contains real-world production-level scripts designed to handle server configurations, system health monitoring, and advanced object-oriented programming (OOP) for DevOps environments.

## 🛠️ Main Project: Core Server Manager (`server_manager.py`)

This is the flagship script of this repository. It integrates multiple core Python modules into a clean, reusable Object-Oriented structure.

### Features:
* **OOPs Architecture:** Built using clean Class and Method structures for better scalability.
* **JSON Parsing (`json` module):** Automatically loads and extracts live configuration strings simulating server metadata.
* **System Monitoring (`os` module):** Automatically fetches the current working directory and underlying operating system details.

### How to Run:
```bash
python3 server_manager.py

🔧 Other Automation Scripts Included:
The Automated Server Pinger: Uses Python's subprocess module to ping remote servers (like Google DNS 8.8.8.8) and verify network availability without leaving the Python environment.

Live API Status Checker: Uses the requests library wrapped inside a robust try-except error handling block to monitor external APIs without crashing.

Advanced Server Management: Implements Object-Oriented inheritance and the super() method to mirror parent-child relations between local and cloud infrastructure (BaseServer vs CloudServer).

# 📈 Technologies Used:

* Language: Python 3

* Core Modules: os, json, subprocess, pathlib

* External Libraries: requests
