import json
import os

File_Name = 'tasks.json'

def load_tasks():
    if os.path.exists(File_Name):
        try:
            with open(File_Name, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
        except Exception as e:
            print(f"An error occurred while loading tasks: {e}")
            return []
    return []

def save_tasks(tasks):
    try:
        with open(File_Name, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2)
    except PermissionError:
        print("Permission denied: Unable to save tasks.")