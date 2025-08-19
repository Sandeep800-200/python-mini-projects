import os
DOLIST = "tasks.txt"
def load_tasks():
    tasks = []
    if os.path.exists(DOLIST):
        with open(DOLIST, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(DOLIST, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📌 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!\n")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑️ Deleted task: {removed}\n")
            else:
                print("❌ Invalid task number.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("===== 📝 To-Do List App =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Your tasks are saved in tasks.txt")
            break
        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()