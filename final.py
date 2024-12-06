# Создаём словарь
note = {}

# Зпишем информацию в словарь с соответствующими ключами
note['username'] = input("Введите имя пользователя: ")
note['content'] = input("Введите описание заметки: ")
note['status'] = input("Введите статус заметки: ")
note['created_date'] = input("Введите дату создания заметки (день-месяц-год): ")
note['issue_date'] = input("Введите дату истчения заметки (день-месяц-год): ")

# Добавляем заголовки
note["titles"] = []
for i in range(3):
    title = input(f"Введите {i + 1} заголовок: ")
    note["titles"].append(title)

# Вывод информации о заметке
print("\nИнформация о заметке: ")
for key, value in note.items():
    print(f"\t{key.capitalize()}: {value}")
