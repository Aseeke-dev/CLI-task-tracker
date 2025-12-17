# CLI Task Tracker

Lightweight command-line task tracker written in Python. Tasks are stored in `tasks.json` as objects with the following properties: `id`, `description`, `status`, `createdAt`, and `updatedAt`.

## Features

- Add tasks with a description
- List tasks (all / done / in-progress / not-done)
- Update task description by id or exact description
- Mark tasks as `in-progress`, `done`, or `todo`
- Delete tasks

## Requirements

- Python 3.7+

## Files

- `task.py` — CLI entrypoint
- `process.py` — core task operations (add, update, mark, delete, list)
- `storage.py` — JSON load/save helper
- `tasks.json` — data file (auto-created)
- `task.bat` — optional batch wrapper for Windows (if present)

## Data model

Each task is an object in `tasks.json` with this schema:

```json
{
	"id": 1,
	"description": "Write tests",
	"status": "todo",          // one of: "todo", "in-progress", "done"
	"createdAt": "2025-12-17T00:44:24.869979Z",
	"updatedAt": "2025-12-17T00:44:40.883721Z"
}
```

Timestamps use ISO 8601 UTC (ending with `Z`).

If the repository previously stored plain string tasks (legacy format), the code will convert them to objects when you mark or update them.

## Usage

Run commands from the project folder. Examples:

```powershell
python task.py add "Buy groceries"
python task.py list
python task.py list-done
python task.py list-inprogress
python task.py list-notdone
python task.py update 2 "Buy fresh vegetables"
python task.py mark 2 in-progress
python task.py mark 2 done
python task.py delete 2
```

Notes:
- For commands that accept an identifier you can pass either the numeric `id` (recommended) or the exact `description` string.
- `list-notdone` shows only tasks with status `todo` (not `in-progress` or `done`).

## Development

- `__pycache__/` and data files are ignored in `.gitignore`.
- To reset all tasks during development you can run a small Python snippet to call `clear_tasks()` from `process.py` or delete `tasks.json`.

## Contributing

Feel free to open issues or submit PRs. Suggestions:
- Add flag-style CLI parsing (argparse / click)
- Add export/import (CSV/JSON)

## Project URL

https://github.com/Aseeke-dev/CLI-task-tracker.git
## License

MIT-style (add your preferred license text).
