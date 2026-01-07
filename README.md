📝 Python CLI Todo App

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

yaml
Copy code

---

## ▶️ How to Run the App

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/moizr1732/todo-cli.git
cd todo-cli
2️⃣ Run the Application
bash
Copy code
python main.py
🧠 How the App Works
Tasks are stored as Python dictionaries

All tasks and user points are saved in a JSON file

The app runs in a loop until the user chooses to exit

Each completed task awards 10 points to encourage productivity

🤖 Use of Claude Code
Claude Code was used as an AI coding assistant to:

Design the overall program structure

Generate initial function templates

Suggest improvements for JSON-based persistence

Help debug runtime errors and refactor logic

All generated code was reviewed, understood, tested, and customized before final submission.

📌 Bonus Features Implemented
File-based persistence using JSON

Task priority and description

Gamification through a points system

Clean menu-driven user experience

🔮 Possible Future Improvements
Filter tasks (Completed / Pending)

Search tasks by keyword

Sort tasks by priority or due date

Colored CLI output

Convert into an installable Python CLI tool

👤 Author
Moiz Ur Rehman
GitHub: https://github.com/moizr1732

📄 License
This project is licensed under the MIT License.

yaml
Copy code

---

## ✅ What to Do Now

1. Open your repo  
2. Edit `README.md`  
3. Paste this content  
4. Commit & push:

```bash
git add README.md
git commit -m "Improve README documentation"
git push
