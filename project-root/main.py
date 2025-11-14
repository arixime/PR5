from auth_module import register, login, logout
from tasks_module import create_task, show_tasks, update_task_status, delete_task
from reports_module import show_statistics, filter_tasks_by_status

def main():
    current_user = None
    
    while True:
        print("СИСТЕМА УПРАВЛЕНИЯ ЗАДАЧАМИ")
        
        if not current_user:
            print("1. Регистрация")
            print("2. Вход")
            print("3. Выход из программы")
        else:
            print(f"Пользователь: {current_user}")
            print("1. Создать задачу")
            print("2. Показать задачи")
            print("3. Изменить статус задачи")
            print("4. Удалить задачу")
            print("5. Статистика")
            print("6. Фильтр по статусу")
            print("7. Выйти из системы")
        
        choice = input("Выберите действие: ").strip()
        
        if not current_user:
            if choice == '1':
                register()
            elif choice == '2':
                current_user = login()
            elif choice == '3':
                print("До свидания!")
                break
            else:
                print("Неверный выбор!")
        
        else:
            if choice == '1':
                create_task(current_user)
            elif choice == '2':
                show_tasks(current_user)
            elif choice == '3':
                update_task_status(current_user)
            elif choice == '4':
                delete_task(current_user)
            elif choice == '5':
                show_statistics(current_user)
            elif choice == '6':
                filter_tasks_by_status(current_user)
            elif choice == '7':
                current_user = logout()
            else:
                print("Неверный выбор!")

if __name__ == "__main__":
    main()