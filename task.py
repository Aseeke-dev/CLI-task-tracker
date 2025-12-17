from process import add_task, list_tasks, update_task, mark_task_inprogress_done, delete_task, list_done_tasks, list_inprogress_tasks, list_tasks_notdone, clear_tasks
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: task [add <description> | list | list-done | list-inprogress | list-notdone | update <id|description> <new description> | mark <id|description> <status> | delete <id|description>]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task to add.")
            return
        task = " ".join(sys.argv[2:])
        new_task = add_task(task)
        if isinstance(new_task, dict):
            print(f"Task added: [{new_task.get('id')}] {new_task.get('description')}")
        else:
            print(f"Task added: {task}")
    elif command == "list":
        list_tasks()
    elif command == "update":
        if len(sys.argv) < 4:
            print("Please provide the task id or description to update and the new description.")
            return
        identifier = sys.argv[2]
        new_description = " ".join(sys.argv[3:])
        update_task(identifier, new_description)
        print(f"Task '{identifier}' updated to '{new_description}'")
    elif command == "mark":
        if len(sys.argv) < 4:
            print("Please provide the task to mark and the status (in-progress/done).")
            return
        status = sys.argv[-1]
        identifier = " ".join(sys.argv[2:-1])
        if not identifier:
            print("Please provide the task id or description to mark and the status (in-progress/done).")
            return
        mark_task_inprogress_done(identifier, status)
        print(f"Task '{identifier}' marked as {status}.")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide the task to delete.")
            return
        task = " ".join(sys.argv[2:])
        delete_task(task)
        print(f"Task deleted: {task}")
    elif command == "list-done":
        list_done_tasks()
    elif command == "list-inprogress":
        list_inprogress_tasks()
    elif command == "list-notdone":
        list_tasks_notdone()
    elif command == "clear":
        clear_tasks()
        print("All tasks cleared.")
    else:
        print("Unknown command. Use 'add' to add a task or 'list' to list tasks.")

if __name__ == "__main__":
    main()