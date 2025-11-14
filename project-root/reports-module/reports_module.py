import os

def show_statistics(email):
    print("\nСТАТИСТИКА")
    
    if not os.path.exists('tasks.txt'):
        print("У вас пока нет задач!")
        return
    
    total_tasks = 0
    todo_count = 0
    inprogress_count = 0
    done_count = 0
    
    with open('tasks.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == email:
                total_tasks += 1
                if parts[3] == "todo":
                    todo_count += 1
                elif parts[3] == "inprogress":
                    inprogress_count += 1
                elif parts[3] == "done":
                    done_count += 1
    
    if total_tasks == 0:
        print("У вас пока нет задач!")
        return
    
    print(f"Всего задач: {total_tasks}")
    print(f"Сделать: {todo_count}")
    print(f"В процессе: {inprogress_count}")
    print(f"Готово: {done_count}")
    
    completion_rate = (done_count / total_tasks) * 100
    print(f"Процент выполнения: {completion_rate:.1f}%")

def filter_tasks_by_status(email):
    print("\nФИЛЬТРАЦИЯ ЗАДАЧ")
    print("1 - Сделать")
    print("2 - В процессе") 
    print("3 - Готово")
    
    choice = input("Выберите статус для фильтра (1-3): ").strip()
    
    status_map = {"1": "todo", "2": "inprogress", "3": "done"}
    if choice not in status_map:
        print("Неверный выбор!")
        return
    
    status = status_map[choice]
    status_rus = "сделать" if status == "todo" else "в процессе" if status == "inprogress" else "готово"
    
    print(f"\nЗадачи со статусом '{status_rus}':")
    
    if not os.path.exists('tasks.txt'):
        print("Задачи не найдены!")
        return
    
    tasks_found = False
    with open('tasks.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == email and parts[3] == status:
                tasks_found = True
                print(f"- {parts[2]}")
    
    if not tasks_found:
        print("Задачи не найдены!")