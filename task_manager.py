import json
import os

TASKS_FILE = "tasks.json"

# Încarcă sarcinile din fișier
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Salvează sarcinile în fișier
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Adaugă o sarcină nouă
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "task": description,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Sarcina adăugată: {description}")

# Afișează toate sarcinile
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nu există sarcini.")
        return
    for task in tasks:
        status = "✔" if task["done"] else "✖"
        print(f'{task["id"]}. [{status}] {task["task"]}')

# Meniul principal
def main():
    while True:
        print("\n=== Task Manager ===")
        print("1. Afișează sarcinile")
        print("2. Adaugă sarcină")
        print("3. Ieșire")

        choice = input("Alege opțiunea: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            description = input("Descrierea sarcinii: ")
            add_task(description)
        elif choice == "3":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă!")
# Marchează o sarcină ca terminată
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Sarcina '{task['task']}' a fost marcată ca terminată!")
            return
    print("Sarcina nu a fost găsită!")

# Șterge o sarcină
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Sarcina '{task['task']}' a fost ștearsă!")
            return
    print("Sarcina nu a fost găsită!")

# Meniul principal actualizat
def main():
    while True:
        print("\n=== Task Manager ===")
        print("1. Afișează sarcinile")
        print("2. Adaugă sarcină")
        print("3. Marchează sarcină ca terminată")
        print("4. Șterge sarcină")
        print("5. Ieșire")

        choice = input("Alege opțiunea: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            description = input("Descrierea sarcinii: ")
            add_task(description)
        elif choice == "3":
            task_id_input = input("ID-ul sarcinii de marcat ca terminată: ")
            if task_id_input.isdigit():
                task_id = int(task_id_input)
                mark_done(task_id)
            else:
                print("⚠️ Te rog introdu un număr valid pentru ID!")

        elif choice == "4":
            task_id_input = input("ID-ul sarcinii de șters: ")
            if task_id_input.isdigit():
                task_id = int(task_id_input)
                delete_task(task_id)
            else:
                print("⚠️ Te rog introdu un număr valid pentru ID!")

if __name__ == "__main__":
    main()
