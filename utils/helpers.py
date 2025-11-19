# utils/helpers.py
# For printing clean table-style output

def print_table(task_list):
    if not task_list:
        print("No tasks found.")
        return

    print("\nID  | Title                 | Status    | Priority | Due Date")
    print("-" * 60)

    for task in task_list:
        status = "Done" if task.completed else "Pending"
        print(f"{task.task_id:<3} | {task.title:<20} | {status:<9} | {task.priority:<8} | {str(task.due_date)}")

    print()
