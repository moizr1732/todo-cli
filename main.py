1
from storage import load_data, save_data

POINTS_PER_TASK = 10

def show_menu():
    print("\n==== TODO APP ====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task complete / incomplete")
    print("4. Update task")
    print("5. Delete task")
    print("6. View points")
    print("0. Exit")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "Done" if task["done"] else "Not Done"
        print(f'''
ID: {task["id"]}
Title: {task["title"]}
Description: {task["description"]}
Priority: {task["priority"]}
Due Date: {task["due_date"]}
Status: {status}
------------------------
''')

def add_task(data):
    tasks = data["tasks"]

    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    description = input("Enter description (optional): ").strip()
    priority = input("Enter priority (Low / Medium / High): ").strip() or "Medium"
    due_date = input("Enter due date (optional): ").strip() or "Not set"

    task_id = tasks[-1]["id"] + 1 if tasks else 1

    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "done": False
    }

    tasks.append(task)
    save_data(data)
    print("Task added successfully.")

def toggle_task(data):
    tasks = data["tasks"]
    list_tasks(tasks)

    try:
        task_id = int(input("Enter task ID: "))
        for task in tasks:
            if task["id"] == task_id:
                if not task["done"]:
                    task["done"] = True
                    data["points"] += POINTS_PER_TASK
                    print(f"Task completed! +{POINTS_PER_TASK} points 🎉")
                else:
                    task["done"] = False
                    print("Task marked as incomplete.")
                save_data(data)
                return
        print("Task not found.")
    except ValueError:
        print("Invalid input.")

def update_task(data):
    tasks = data["tasks"]
    list_tasks(tasks)

    try:
        task_id = int(input("Enter task ID to update: "))
        for task in tasks:
            if task["id"] == task_id:
                new_title = input("New title (leave blank to keep same): ").strip()
                new_desc = input("New description (leave blank to keep same): ").strip()
                new_priority = input("New priority (leave blank to keep same): ").strip()
                new_due = input("New due date (leave blank to keep same): ").strip()

                if new_title:
                    task["title"] = new_title
                if new_desc:
                    task["description"] = new_desc
                if new_priority:
                    task["priority"] = new_priority
                if new_due:
                    task["due_date"] = new_due

                save_data(data)
                print("Task updated successfully.")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid input.")

def delete_task(data):
    tasks = data["tasks"]
    list_tasks(tasks)

    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_data(data)
                print("Task deleted successfully.")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid input.")

def view_points(data):
    print(f"🏆 Total Points: {data['points']}")

def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(data)
        elif choice == "2":
            list_tasks(data["tasks"])
        elif choice == "3":
            toggle_task(data)
        elif choice == "4":
            update_task(data)
        elif choice == "5":
            delete_task(data)
        elif choice == "6":
            view_points(data)
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
