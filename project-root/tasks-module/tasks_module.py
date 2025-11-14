import os

def create_task(email):
    print("\nСОЗДАНИЕ ЗАДАЧИ")
    title = input("Введите название задачи: ").strip()
    if not title:
        print("Название не может быть пустым!")
        return
    
    # Загрузка существующих задач
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 4 and parts[0] == email:
                    tasks.append(parts)
    
    # Создание новой задачи
    task_id = len(tasks) + 1
    with open('tasks.txt', 'a') as f:
        f.write(f"{email}:{task_id}:{title}:todo\n")
    print("Задача создана!")

def show_tasks(email):
    print("\nВАШИ ЗАДАЧИ")
    
    if not os.path.exists('tasks.txt'):
        print("У вас пока нет задач!")
        return
    
    tasks_found = False
    with open('tasks.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == email:
                tasks_found = True
                status_rus = "сделать" if parts[3] == "todo" else "в процессе" if parts[3] == "inprogress" else "готово"
                print(f"{parts[1]}. {parts[2]} - {status_rus}")
    
    if not tasks_found:
        print("У вас пока нет задач!")

def update_task_status(email):
    show_tasks(email)
    
    try:
        task_id = input("Введите ID задачи: ").strip()
        if not task_id:
            return
        
        print("Статусы: 1 - Сделать, 2 - В процессе, 3 - Готово")
        status_choice = input("Выберите статус (1-3): ").strip()
        
        status_map = {"1": "todo", "2": "inprogress", "3": "done"}
        if status_choice not in status_map:
            print("Неверный выбор статуса!")
            return
        
        new_status = status_map[status_choice]
        
        # Обновление статуса задачи
        tasks = []
        updated = False
        
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as f:
                for line in f:
                    parts = line.strip().split(':')
                    if len(parts) == 4 and parts[0] == email and parts[1] == task_id:
                        parts[3] = new_status
                        updated = True
                    tasks.append(parts)
        
        if updated:
            # Перезапись файла
            with open('tasks.txt', 'w') as f:
                for task in tasks:
                    f.write(':'.join(task) + '\n')
            print("Статус задачи обновлен!")
        else:
            print("Задача не найдена!")
            
    except Exception as e:
        print("Ошибка при обновлении задачи!")

def delete_task(email):
    show_tasks(email)
    
    task_id = input("Введите ID задачи для удаления: ").strip()
    if not task_id:
        return
    
    # Удаление задачи
    tasks = []
    deleted = False
    
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 4:
                    if not (parts[0] == email and parts[1] == task_id):
                        tasks.append(parts)
                    else:
                        deleted = True
    
    if deleted:
        with open('tasks.txt', 'w') as f:
            for task in tasks:
                f.write(':'.join(task) + '\n')
        print("Задача удалена!")
    else:
        print("Задача не найдена!")