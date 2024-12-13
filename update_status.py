from time import sleep

# Создаём словарь
note = {}

# Запрашиваем основные данные у пользователя
note['username'] = input("Введите имя пользователя: ")
note['content'] = input("Введите описание заметки: ")
note['created_date'] = input("Введите дату создания заметки (день-месяц-год): ")
note['issue_date'] = input("Введите дату истчения заметки (день-месяц-год): ")

# Добавляем заголовки
note['titles'] = []
new_title = input("Введите новый заголовок (или оставьте строку ввода пустой для завершения): ")
while new_title != '':
    if new_title in note['titles']:
        new_title = input("Данный заголовок уже существует, введите другой (или оставьте строку ввода пустой для завершения): ")
        sleep(150)
    else:
        note['titles'].append(new_title)
        print("Добавлен новый заголовок: ", new_title)
        new_title = input("Введите новый заголовок (или оставьте строку ввода пустой для завершения): ")

# Оповещение пользователя об окончании добавления заголовков
print('Вы закончили ввод заголовков')

# Задаём список готовых статусов
statuses = ['выполнено', 'в процессе', 'отложено']

# Запрашиваем варианты у пользователя
status_num = input("Выберите статус и введите его номер:\n"
                       f"\t1. {statuses[0]}\n"
                       f"\t2. {statuses[1]}\n"
                       f"\t3. {statuses[2]}\n")

# Проверяем корректность ввода
while status_num not in ['1', '2', '3']:
    status_num = input("Введено некорректное значение. Введите число в диапозоне 1-3: ")

# Изменяем статус заметки
note['status'] = statuses[int(status_num) - 1]

# Сообщаем пользователю об успешном изменении статуса
print(f"Статус заметки изменён на {statuses[int(status_num) - 1].upper()}")

# Спрашиваем у пользователя, хочет ли он заменить статус
answer = input("Хотите изменить статус заметки? Введите Y (да) или N (нет): ")

# Проверяем на корректность
while answer.upper() not in ['Y', 'N']:
    answer = input("Введено некорректное значение, повторите ввод: ")

# С помощью if проверяем, хочет ли пользователь изменить статус
if answer.upper() == 'Y':
    status_num = input("Выберите статус и введите его номер:\n"
                       f"\t1. {statuses[0]}\n"
                       f"\t2. {statuses[1]}\n"
                       f"\t3. {statuses[2]}\n")
    while status_num not in ['1', '2', '3']:
        status_num = input("Введено некорректное значение. Введите число в диапозоне 1-3: ")
    note['status'] = statuses[int(status_num) - 1]

# Выводим информацию о заметке
print('\nИнформация о заметке:')
for key, value in note.items():
    if key != 'titles':
        print(f"\t{key.capitalize()}: {value}")
print("Заголовки заметки:")
for title in note['titles']:
    print("\t- ", title)