# Create a Task class with a description and due_date (both strings).
# Define an __init__ method, then try creating three instances of this class.


class Task:

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date


task1 = Task("laundry", "Feb 21")
print(task1.description)
print(task1.due_date)

task2 = Task("buy groceries", "Feb 23")
print(task2.description)
print(task2.due_date)

task3 = Task("go to bank", "Feb 24")
print(task3.description)
print(task3.due_date)
