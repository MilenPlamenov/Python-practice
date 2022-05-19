class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task.name not in [t.name for t in self.tasks]:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        if task_name not in [t.name for t in self.tasks]:
            return f"Could not find task with the name {task_name}"
        searched_task = [t for t in self.tasks if t.name == task_name][0]
        searched_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = [t for t in self.tasks if t.completed]
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        data = ''
        data += f"Section {self.name}:\n"
        data += ''.join([f"{t.details()}\n" for t in self.tasks])
        return data
