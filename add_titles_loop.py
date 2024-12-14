# Создаём словарь
some_note = {}

# Запрашиваем основные данные у пользователя
some_note['username'] = input("Введите имя пользователя: ")
some_note['content'] = input("Введите описание заметки: ")
some_note['status'] = input("Введите статус заметки: ")
some_note['created_date'] = input("Введите дату создания заметки (день-месяц-год): ")
some_note['issue_date'] = input("Введите дату истчения заметки (день-месяц-год): ")

# Добавляем заголовки
some_note['titles'] = []
new_title = input("Введите новый заголовок (или оставьте строку ввода пустой для завершения): ")
while new_title != '':
    if new_title in some_note['titles']:
        new_title = input("Данный заголовок уже существует, введите другой "
                          "(или оставьте строку ввода пустой для завершения): ")
    else:
        some_note['titles'].append(new_title)
        print("Добавлен нлвый заголовок: ", new_title)
        new_title = input("Введите новый заголовок (или оставьте строку ввода пустой для завершения): ")

# Оповещение пользователя об окончании добавления заголовков
print('Вы закончили ввод заголовков')

# Вывод информации о заметке
print('\nИнформация о заметке:')
for key, value in some_note.items():
    if key != 'titles':
        print(f"\t{key.capitalize()}: {value}")
    else:
        print("Заголовки заметки:")
        for title in some_note['titles']:
            print(f"\t- {title}")
