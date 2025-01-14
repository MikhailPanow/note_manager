# Создаём словарь
some_note = {}

# Зпишем информацию в словарь с соответствующими ключами
some_note['username'] = input("Введите имя пользователя: ")
some_note['content'] = input("Введите описание заметки: ")
some_note['status'] = input("Введите статус заметки: ")
some_note['created_date'] = input("Введите дату создания заметки (день-месяц-год): ")
some_note['issue_date'] = input("Введите дату истчения заметки (день-месяц-год): ")

# Добавляем заголовки
some_note["titles"] = []
for i in range(3):
    title = input(f"Введите {i + 1} заголовок: ")
    some_note["titles"].append(title)

# Вывод информации о заметке
print("\nИнформация о заметке: ")
for key, value in some_note.items():
    print(f"\t{key.capitalize()}: {value}")
