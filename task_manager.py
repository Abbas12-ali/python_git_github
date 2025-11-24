import json
from models.task import Task

TASKS_FILE = "data/tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(TASKS_FILE, "r") as file:
                data = json.load(file)
                self.tasks = [Task(**item) for item in data]
        except():
            self.tasks = []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, priority="Normal", due_date=None):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, False, priority, due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def update_task(self, task_id, new_title):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title
                self.save_tasks()
                return True
        return False

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        # Fix IDs after delete
        for i, task in enumerate(self.tasks, start=1):
            task.task_id = i
        self.save_tasks()

    def search_tasks(self, keyword):
        return [t for t in self.tasks if keyword.lower() in t.title.lower()]

    def get_tasks(self, show_completed=None):
        if show_completed is None:
            return self.tasks
        return [t for t in self.tasks if t.completed == show_completed]
