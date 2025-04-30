from datetime import datetime
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete" 
    def mark_complete(self):
        self.status = "Complete"
    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {self.status}"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title and task.status == "Incomplete":
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found or already completed.")
    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nAll Tasks:")
            for task in self.tasks:
                print(task)
    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete_tasks:
            print("No incomplete tasks.")
        else:
            print("\nIncomplete Tasks:")
            for task in incomplete_tasks:
                print(task)
def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                datetime.strptime(due_date, "%Y-%m-%d") 
                todo_list.add_task(title, description, due_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)
        elif choice == "3":
            todo_list.list_all_tasks()
        elif choice == "4":
            todo_list.list_incomplete_tasks()
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()