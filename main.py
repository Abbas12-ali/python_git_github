# main.py
# Main entry point of the program

from task_manager import TaskManager
from utils.helpers import print_table

def menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Show all tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Mark task as complete")
    print("5. Delete task")
    print("6. Search tasks")
    print("7. Show only completed tasks")
    print("8. Show only pending tasks")
    print("0. Exit")


def main():
    manager = TaskManager()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            print_table(manager.get_tasks())

        elif choice == "2":
            title = input("Task title: ")
            priority = input("Priority (Low/Normal/High): ") or "Normal"
            due_date = input("Due date (optional): ") or None
            manager.add_task(title, priority, due_date)
            print("Task added!")

        elif choice == "3":
            task_id = int(input("Task ID to update: "))
            new_title = input("New title: ")
            if manager.update_task(task_id, new_title):
                print("Updated successfully!")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = int(input("Task ID to mark complete: "))
            if manager.mark_complete(task_id):
                print("Marked complete!")
            else:
                print("Task not found.")

        elif choice == "5":
            task_id = int(input("Task ID to delete: "))
            manager.delete_task(task_id)
            print("Deleted!")

        elif choice == "6":
            keyword = input("Search keyword: ")
            results = manager.search_tasks(keyword)
            print_table(results)

        elif choice == "7":
            print_table(manager.get_tasks(show_completed=True))

        elif choice == "8":
            print_table(manager.get_tasks(show_completed=False))

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
