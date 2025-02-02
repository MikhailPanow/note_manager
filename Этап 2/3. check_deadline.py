'''ИНИЦИАЛИЗАЦИЯ'''

# Подключение datetime для работы с датами
import datetime

# Функция подписи дней
def days_write(days):
    try:
        if 11 <= int(days[-3:]) <= 19:
            return 'дней'
    except IndexError:
        if 2 <= int(days[-1]) <= 4:
            return 'дня'
        elif int(days[-1]) == 1:
            return 'день'
        else:
            return 'дней'

# Функция ввода даты от пользователя в корректном виде
def set_issue_date(note):
    issue_date = input('Введите дату истечения заметки в формате ГГГГ-ММ-ДД или ДД-ММ-ГГГГ: ')
    try:
        issue_date = datetime.datetime.strptime(issue_date, '%d-%m-%Y').date()
        note['issue_date'] = issue_date
        return True
    except ValueError:
        try:
            issue_date = datetime.datetime.strptime(issue_date, '%Y-%m-%d').date()
            note['issue_date'] = issue_date
        except ValueError:
            print('Неверно введённый формат даты, повторите ввод')

# Проверка дедлайна
def check_deadline(note):
    issue_date = note['issue_date']
    created_date = note['created_date']
    deadline_delta = (issue_date - created_date).days
    if deadline_delta > 2:
        print(f'\t- До дедлайна {deadline_delta} {days_write(deadline_delta)}')
    elif deadline_delta == 2:
        print('\t- Дедлайн послезавтра')
    elif deadline_delta == 1:
        print('\t- Дедлайн завтра')
    elif deadline_delta == 0:
        print('\t- Дедлайн сегодня!')
    elif deadline_delta == -1:
        print('\t- Дедлайн был вчера!')
    elif deadline_delta == -2:
        print('\t- Дедлайн был позавчера!')
    else:
        print(f'\t- Дедлайн был {deadline_delta[1:]} {days_write(deadline_delta)} назад!')

# Функция для запроса данных от пользователя
def set_info(note):
    note['username'] = input("Введите имя пользователя: ")
    note['content'] = input("Введите описание заметки: ")
    return note


# Функция ввода заголовков
def add_titles(note):
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
    note['titles'] = titles

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
    print("\tДедлайн:")
    check_deadline(note)

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
