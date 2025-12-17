from storage import load_tasks, save_tasks
from datetime import datetime
from typing import Optional


def _now_iso():
    return datetime.utcnow().isoformat() + "Z"


def _next_id(tasks):
    if not tasks:
        return 1
    ids = [t.get('id', 0) for t in tasks if isinstance(t, dict)]
    return max(ids, default=0) + 1


def add_task(description: str):
    tasks = load_tasks()
    task = {
        "id": _next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": _now_iso(),
        "updatedAt": _now_iso()
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks():
    tasks = load_tasks()
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            if isinstance(task, dict):
                print(f"{idx}. [{task.get('id')}] {task.get('description')} - {task.get('status')} (updated: {task.get('updatedAt')})")
            else:
                print(f"{idx}. {task}")
    else:
        print("No task found.")


def _find_task(tasks, identifier) -> Optional[int]:
    try:
        iid = int(identifier)
    except Exception:
        iid = None

    for idx, t in enumerate(tasks):
        if isinstance(t, dict):
            if iid is not None and t.get('id') == iid:
                return idx
            if t.get('description') == identifier:
                return idx
        else:
            if identifier == t:
                return idx
    return None


def update_task(identifier, new_description):
    tasks = load_tasks()
    idx = _find_task(tasks, identifier)
    if idx is not None:
        t = tasks[idx]
        if isinstance(t, dict):
            t['description'] = new_description
            t['updatedAt'] = _now_iso()
            tasks[idx] = t
        else:
            tasks[idx] = new_description
        save_tasks(tasks)
    else:
        print("Task not found.")


def _normalize_status(s: str) -> str:
    s = s.strip().lower()
    if s in ("inprogress", "in-progress", "in progress", "in_progress", "in"):
        return "in-progress"
    if s in ("done", "complete", "finished"):
        return "done"
    if s in ("todo", "to-do", "to do"):
        return "todo"
    return s


def mark_task_inprogress_done(identifier, status):
    tasks = load_tasks()
    idx = _find_task(tasks, identifier)
    if idx is None:
        print("Task not found.")
        return

    new_status = _normalize_status(status)
    t = tasks[idx]
    if isinstance(t, dict):
        t['status'] = new_status
        t['updatedAt'] = _now_iso()
        tasks[idx] = t
        save_tasks(tasks)
    else:
        task_obj = {
            'id': _next_id([x for x in tasks if isinstance(x, dict)]),
            'description': t,
            'status': new_status,
            'createdAt': _now_iso(),
            'updatedAt': _now_iso()
        }
        tasks[idx] = task_obj
        save_tasks(tasks)


def delete_task(identifier):
    tasks = load_tasks()
    idx = _find_task(tasks, identifier)
    if idx is not None:
        tasks.pop(idx)
        save_tasks(tasks)
    else:
        print("Task not found.")


def list_done_tasks():
    tasks = load_tasks()
    done_tasks = [t for t in tasks if isinstance(t, dict) and t.get('status') == 'done']
    for idx, task in enumerate(done_tasks, start=1):
        print(f"{idx}. [{task.get('id')}] {task.get('description')} - {task.get('status')}")


def list_inprogress_tasks():
    tasks = load_tasks()
    inprogress_tasks = [t for t in tasks if isinstance(t, dict) and t.get('status') == 'in-progress']
    for idx, task in enumerate(inprogress_tasks, start=1):
        print(f"{idx}. [{task.get('id')}] {task.get('description')} - {task.get('status')}")


def list_tasks_notdone():
    tasks = load_tasks()
    not_done_tasks = [t for t in tasks if isinstance(t, dict) and t.get('status') == 'todo']
    for idx, task in enumerate(not_done_tasks, start=1):
        print(f"{idx}. [{task.get('id')}] {task.get('description')} - {task.get('status')}")


def clear_tasks():
    save_tasks([])