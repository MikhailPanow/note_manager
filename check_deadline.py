'''ИНИЦИАЛИЗАЦИЯ'''
# Подключение datetime для работы с датами
import datetime

# Функция для запроса данных от пользователя
def set_info():
    global some_note
    some_note['username'] = input("Введите имя пользователя: ")
    some_note['content'] = input("Введите описание заметки: ")
    some_note['created_date'] = input("Введите дату создания заметки (день-месяц-год): ")
    some_note['issue_date'] = input("Введите дату истчения заметки (день-месяц-год): ")


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
def get_info():
    global some_note
    print('\nИнформация о заметке:')
    for key, value in some_note.items():
        if key != 'titles':
            print(f"\t{key.capitalize()}: {value}")
    print("Заголовки заметки:")
    for title in some_note['titles']:
        print("\t- ", title)

# Создаём словарь
some_note = {}


'''ОСНОВНОЙ БЛОК КОДА'''

# Запрашиваем информацию у пользователя
set_info()

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
get_info()