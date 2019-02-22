# Create a TodoList class with a tasks list (which will contain instances
# of the Task class). Create an __init__ method and an add_task method that
# allows you to pass in an instance of your Task class.
# Try creating a todo list and adding your three tasks to it.

from task import Task


class ToDo:

    todo_list = []

    def __init__(self, tasks):
        self.tasks = tasks

    @classmethod
    def add_task(cls, description, due_date):
        new_task = Task(description, due_date)
        cls.todo_list.append(new_task)
        return cls.todo_list


task1 = ToDo.add_task("laundry", "Feb 22")
task2 = ToDo.add_task("buy groceries", "Feb 23")
task3 = ToDo.add_task("go to bank", "Feb 24")
print(len(ToDo.todo_list))  # 3
print(ToDo.todo_list[1].description)  # 'buy groceries'
