import os

def register():
    print("\nРЕГИСТРАЦИЯ")
    email = input("Введите email: ").strip()
    if '@' not in email or '.' not in email:
        print("Email должен содержать '@' и '.'")
        return None
    
    password = input("Введите пароль (минимум 6 символов): ")
    if len(password) < 6:
        print("Пароль слишком короткий!")
        return None
    
    # Проверка существования пользователя
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if parts[0] == email:
                    print("Email уже зарегистрирован!")
                    return None
    
    # Запись нового пользователя
    with open('users.txt', 'a') as f:
        f.write(f"{email}:{password}\n")
    print("Регистрация успешна!")
    return email

def login():
    print("\nВХОД")
    email = input("Введите email: ").strip()
    password = input("Введите пароль: ").strip()
    
    if not os.path.exists('users.txt'):
        print("Нет зарегистрированных пользователей!")
        return None
    
    with open('users.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            if parts[0] == email and parts[1] == password:
                print(f"Вход выполнен! Добро пожаловать, {email}!")
                return email
    
    print("Неверный email или пароль!")
    return None

def logout():
    print("Выход из системы!")
    return None