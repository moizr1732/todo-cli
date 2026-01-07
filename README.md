# 📝 Python CLI Todo App

A beginner-friendly **Command Line Todo Application** built using **Python**, designed to help users manage daily tasks efficiently from the terminal.  
This project was developed as part of **Assignment 1: Python CLI Todo App (with Claude Code Assistance)**.

---

## 🚀 Features

- ➕ Add new tasks with:
  - Title
  - Optional description
  - Priority (Low / Medium / High)
  - Optional due date
- 📋 View all tasks in a clean CLI format
- ✅ Mark tasks as complete or incomplete
- ✏️ Update existing tasks
- 🗑️ Delete tasks
- 🏆 **Points System**:
  - Earn **10 points** for each completed task
  - View total points anytime
- 💾 Persistent storage using `JSON` (tasks are saved even after exit)
- ⚠️ Basic error handling for invalid inputs

---

## 🛠️ Technologies Used

- Python 3
- JSON (for file-based data storage)
- Command Line Interface (CLI)

---

## 📁 Project Structure
todo-cli/
├── main.py # Main application logic
├── storage.py # File handling (load/save JSON)
├── README.md # Project documentation
└── tasks.json # Auto-generated (ignored in Git)

---

## ▶️ How to Run the App

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/moizr1732/todo-cli.git
cd todo-cli

