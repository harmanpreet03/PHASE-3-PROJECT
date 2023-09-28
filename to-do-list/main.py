from config import get_session, init_db
from models import TodoList, Task

def create_todo_list(session):
    name = input("Enter the name of your to-do list: ")
    todo_list = TodoList(name=name)
    session.add(todo_list)
    session.commit()
    print(f"To-Do list '{name}' created successfully!")

def create_task(session):
    todolists = session.query(TodoList).all()
    if not todolists:
        print("No to-do lists available. Create a to-do list first.")
        return

    print("Select a to-do list to add the task:")
    for idx, todolist in enumerate(todolists):
        print(f"{idx + 1}. {todolist}")

    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(todolists):
            selected_list = todolists[choice - 1]
            description = input("Enter the task description: ")
            task = Task(description=description, todolist=selected_list)
            session.add(task)
            session.commit()
            print(f"Task '{description}' added to '{selected_list}' successfully!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_tasks(session):
    tasks = session.query(Task).all()
    if tasks:
        print("\nTasks:")
        for task in tasks:
            print(f"- {task} (Completed: {task.completed})")
    else:
        print("No tasks available.")

def mark_task_complete(session):
    tasks = session.query(Task).filter(Task.completed.is_(False)).all()
    if not tasks:
        print("No incomplete tasks available.")
        return

    print("Select a task to mark as complete:")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(tasks):
            selected_task = tasks[choice - 1]
            selected_task.completed = True
            session.commit()
            print(f"Task '{selected_task.description}' marked as complete.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    init_db()
    session = get_session()

    while True:
        print("\nOptions:")
        print("1. Create To-Do List")
        print("2. Add Task")
        print("3. View Tasks")
        print("4. Mark Task as Complete")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_todo_list(session)
        elif choice == '2':
            create_task(session)
        elif choice == '3':
            view_tasks(session)
        elif choice == '4':
            mark_task_complete(session)
        elif choice == '5':
            session.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
