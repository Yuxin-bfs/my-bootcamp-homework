# to_do_list.py
tasks = []


def add_task(description):
    task = {"description": description, "completed": False}
    tasks.append(task)


def mark_task_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Task index out of range.")


def view_tasks():
    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}: {task['description']} [{status}]")


# Example usage

if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("Read a book")
    mark_task_complete(0)
    mark_task_complete(1)
    view_tasks()
