class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.task_stack = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.task_stack.append(task)

    def mark_task_as_completed(self):
        if not self.task_stack:
            print("No tasks to mark as completed.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.task_stack):
                print(f"{index + 1}. {task.title} ({'Completed' if task.completed else 'Incomplete'})")
            
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(self.task_stack):
                self.task_stack[task_index].completed = True
                print(f"{self.task_stack[task_index].title} marked as completed.")
            else:
                print("Invalid task number. No task marked as completed.")

    def display_tasks(self):
        if not self.task_stack:
            print("No tasks.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.task_stack):
                print(f"{index + 1}. {task.title} - {task.description} ({'Completed' if task.completed else 'Incomplete'})")

    def run(self):
        while True:
            print("Task Manager Menu:")
            print("1. Add Task")
            print("2. Mark Task as Completed")
            print("3. Display Tasks")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                self.add_task(title, description)
                print("Task added successfully.")
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
