# models/task.py

class Task:
    def __init__(self, task_id, title, priority="Medium", due_date=None, completed=False):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed
        }
