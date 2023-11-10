class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_as_completed(self):
        if not self.tasks:
            print("No tasks to mark as completed.")
        else:
            self.display_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index].completed = True
                print(f"{self.tasks[task_index].title} marked as completed.")
            else:
                print("Invalid task number. No task marked as completed.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Incomplete"
                print(f"{index}. {task.title} - {task.description} ({status})")

    def run(self):
        while True:
            print("Task Manager Menu:")
            print("1. Add Task")
            print("2. Mark Task as Completed")
            print("3. Display Tasks")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.mark_task_as_completed()
            elif choice == '3':
                self.display_tasks()
            elif choice == '4':
                print("Closing Task Manager...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
