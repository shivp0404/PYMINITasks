import json
import os
from task import Task

# Get current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create 'data' folder path relative to this script
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)  # create 'data/' if not exists

# Final path to the task file
TASK_FILE = os.path.join(DATA_DIR, "tasks.json")

task_list = []

def load_tasks():
    global task_list
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,'r') as f:
            data = json.load(f)
            task_list = [Task.from_dict(t) for t in data]

def save_tasks():
    with open(TASK_FILE,'w') as f:
        json.dump([t.to_dict() for t in task_list],f,indent =2)


def add_task():
    title = input("Enter task title")
    category = input("Enter Category")
    task = Task(title,category)
    task_list.append(task)
    print("Task Added.")


def view_task():
    if not task_list:
        print("No tasks found")
        return
    print("YOur Tasks:\n")
    for i, task in enumerate(task_list,1):
        status =  "✅" if task.done else "❌"
        print(f"{i}. {task.title} [{task.category}]-{status}-{task.created_at}")

def mark_task_done():
    view_task()
    idx = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= idx < len(task_list):
        task_list[idx].mark_done()
        print("🎉 Task marked as done.")
    else:
        print("❌ Invalid task number.")

def menu():
    while True:
        print("\n--- PyMiniTasks Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            save_tasks()
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    load_tasks()
    menu()