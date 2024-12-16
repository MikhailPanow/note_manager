'''ИНИЦИАЛИЗАЦИЯ'''

# Подключение datetime для работы с датами
import datetime

# Функция ввода даты от пользователя в корректном виде
def set_issue_date(note):
    issue_date = input('Введите дату истечения заметки в формате ГГГГ-ММ-ДД или ДД-ММ-ГГГГ: ').split('-')
    if len(issue_date) == 3:
        for date in issue_date:
            if not date.isdigit():
                return False
        if len(issue_date[1]) == len(issue_date[2]) == 2:
            if len(issue_date[0]) == 4:
                issue_date = '-'.join(issue_date)
                try:
                    issue_date = datetime.datetime.strptime(issue_date, '%Y-%m-%d')
                except ValueError:
                    return False
            else:
                return False
        elif len(issue_date[0]) == len(issue_date[1]) == 2:
            if len(issue_date[2]) == 4:
                issue_date = '-'.join(issue_date)
                try:
                    issue_date = datetime.datetime.strptime(issue_date, '%d-%m-%Y')
                except ValueError:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    note['issue_date'] = issue_date.date()
    return True

# Функция для запроса данных от пользователя
def set_info(note):
    note['username'] = input("Введите имя пользователя: ")
    note['content'] = input("Введите описание заметки: ")
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
    print("\tЗаголовки заметки:")
    for title in note['titles']:
        print("\t- ", title)

# Создаём словарь
some_note = {}


'''ОСНОВНОЙ БЛОК КОДА'''

# Запрашиваем основную информацию у пользователя
set_info(some_note)

# Запрашиваем циклично дату у пользователя, пока она не будет корректной
while not set_issue_date(some_note):
    print('Повторите ввод')

# Запись сегодняшней даты
some_note['created_date'] = datetime.date.today()

# Запись заголовков
some_note['titles'] = add_titles()

# Вывод информации
get_info(some_note)
