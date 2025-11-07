# 🧠 Smart Assistant using Python

A desktop-based **AI-powered Smart Assistant** built with **Python** and **Eel**, designed to perform automated tasks, respond to voice commands, and integrate with a modern web interface.

---

Developed by Ganapurapu Durga Srinath.
If you find this project interesting, please ⭐ the repo and share your thoughts!

---

## 🚀 Overview

This project is a **personal AI assistant** that can listen, respond, and execute basic computer operations or custom commands.  
It uses **Python** for the backend logic and **Eel** to serve a lightweight, interactive web interface built with HTML, CSS, and JavaScript.

---

## 🧰 Tech Stack

- **Language:** Python 🐍  
- **Framework:** [Eel](https://github.com/ChrisKnott/Eel) (Python ↔️ JavaScript bridge)
- **Frontend:** HTML, CSS, JavaScript  
- **Modules:**  
  - `os` — for system operations  
  - `eel` — to connect Python with the web interface  
  - Custom modules in `/engine` for features and command handling

---

## 📁 Project Structure


Smart-Assistant/
│
├── engine/
│ ├── features.py # Core assistant features
│ ├── command.py # Command handling logic
│
├── www/
│ ├── index.html # Frontend UI
│ ├── assets/ # Images, icons, etc.
│
├── main.py # Entry point (launches the assistant)
└── README.md # Project documentation

🧠 How It Works

The Python backend handles logic, features, and voice responses.
Eel creates a bridge between Python and a web-based UI.
The assistant starts a local web server and opens the interface automatically.
Custom modules in the engine/ folder define its abilities — you can extend them for more smart features.



🚧 Future Plans
This project is just the start — upcoming improvements can include:

🎙️ Advanced voice recognition & NLP

🌐 Integration with APIs (weather, news, etc.)

💡 Smart home device control

📅 Task scheduling & reminders

📱 Cross-platform UI support


“A simple voice today can drive the smart home of tomorrow.”
— Ganapurapu Durga Srinath

---

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/srinadhnaiduu/smart-assistant.git
cd smart-assistant


