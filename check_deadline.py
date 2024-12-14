'''ИНИЦИАЛИЗАЦИЯ'''

# Подключение datetime для работы с датами
import datetime

# Функция форматирования даты
def format_date(note):
    issue_date = note['issue_date']
    if issue_date[:4].isdigit():
        year = int(issue_date[:4])
        month = int(issue_date[5:7])
        day = int(issue_date[8:10])
    else:
        year = int(issue_date[6:10])
        month = int(issue_date[3:5])
        day = int(issue_date[:2])
    issue_date = datetime.date(year, month, day)
    return issue_date

# Функция для запроса данных от пользователя
def set_info(note):
    note['username'] = input("Введите имя пользователя: ")
    note['content'] = input("Введите описание заметки: ")
    note['created_date'] = input("Введите дату создания заметки (день-месяц-год): ")
    note['issue_date'] = input("Введите дату истчения заметки (день-месяц-год): ")
    return note


# Функция ввода заголовков
def add_titles():
    titles = []
    new_title = input("Введите новый заголовок (или оставьте строку ввода пустой для завершения): ")
    while new_title != '':
        if new_title in titles:
            new_title = input("Данный заголовок уже существует, введите другой "
                              "(или оставьте строку ввода пустой для завершения): ")
        else:
            titles.append(new_title)
            print("Добавлен новый заголовок: ", new_title)
            new_title = input("Введите новый заголовок (или оставьте строку ввода пустой для завершения): ")
    return titles

# Функция первичного ввода статуса
def first_status():
    statuses = ['1', '2', '3', 'выполнено', 'отложено', 'в процессе']
    status = input(f'Введите номер статус или наберите его текстом:\n'
                   f'\t{statuses[0]}: {statuses[3].upper()}\n'
                   f'\t{statuses[1]}: {statuses[4].upper()}\n'
                   f'\t{statuses[2]}: {statuses[5].upper()}\n')
    while status not in statuses:
        status = input('Введено некорректное значение, повторите ввод: ')
    if status.isdigit():
        print(f'Статус заметки изменён на {statuses[int(status) + 2].upper()}')
        return statuses[int(status) + 2]
    else:
        print(f'Статус заметки изменён на {status}')
        return status

# Функция замены статуса
def change_status(note):
    statuses = ['1', '2', '3', 'ВЫПОЛНЕНО', 'ОТЛОЖЕНО', 'В ПРОЦЕССЕ']
    status = note['status']
    answer = input("Хотите изменить статус заметки? Введите Y (да) или N (нет): ")
    while answer.upper() != "N":
        while answer.upper() not in ['Y', 'N']:  # Проверка на корректность
            answer = input("Введено некорректное значение, повторите ввод: ")
            if answer.upper() == 'N':
                print(f'Вы решили не изменять статус {status.upper()}')
                return note
        if answer.upper() == 'Y':
            status = input(f'Введите номер статус или наберите его текстом:\n'
                           f'\t{statuses[0]}: {statuses[3].upper()}\n'
                           f'\t{statuses[1]}: {statuses[4].upper()}\n'
                           f'\t{statuses[2]}: {statuses[5].upper()}\n')

            # Проверка на корректность
            while status.upper() not in statuses:
                status = input("Введено некорректное значение. Введите число в диапозоне 1-3 или статус целиком: ")

            # Изменяем статус
            if status.isdigit():
                print(f'Статус успешно изменён на {statuses[int(status) + 2].upper()}')
                status = statuses[int(status) + 2]
            else:
                print(f'Статус успешно изменён на {status.upper()}')

        answer = input("Хотите изменить статус заметки? Введите Y (да) или N (нет): ")
    note['status'] = status
    return note

# Вывод информации
def get_info(note):
    print('\nИнформация о заметке:')
    for key, value in note.items():
        if key != 'titles':
            print(f"\t{key.capitalize()}: {value}")
    print("Заголовки заметки:")
    for title in note['titles']:
        print("\t- ", title)

# Создаём словарь
some_note = {}


'''ОСНОВНОЙ БЛОК КОДА'''

# Запрашиваем информацию у пользователя
some_note = set_info(some_note)

# Форматирование даты (проверка)
some_note['issue_date'] = format_date(some_note)
print(some_note['issue_date'])

# Добавляем заголовки
some_note['titles'] = []
some_note['titles'] += add_titles()

# Оповещение пользователя об окончании добавления заголовков
print('Вы закончили ввод заголовков')

# Первичный запрос статуса у пользователя
some_note['status'] = first_status()

# Цикличный запрос на изменение статуса
some_note = change_status(some_note)

# Выводим информацию о заметке
get_info(some_note)
