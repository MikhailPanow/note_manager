'''ИНИЦИАЛИЗАЦИЯ'''

# Подключение datetime для работы с датами
import datetime

# Подключение init библиотеки colorama для инициализации
from colorama import init

# Подключение изменения цвета текста, фона и стиля написания
from colorama import Fore, Back, Style

# Глобальная переменная словаря записок (ID(ключ):some_note(значение))
note_saver = {}

# Глобальная переменная ID
note_id = 1

# Обновление заметки
def update_note():
    global note_saver
    display_notes(note_saver)
    if not note_saver:
        return
    note_number = input('Введите номер заметки, которую хотите изменить: ')
    note_number = check_answer(list(note_saver.keys()), note_number)
    note = note_saver[note_number]
    print('Текущие данные заметки: ')
    get_info(note)
    changes = ['1', '2', '3', '4', '5',
               'ИМЯ ПОЛЬЗОВАТЕЛЯ', 'ЗАГОЛОВКИ',
               'ОПИСАНИЕ', 'СТАТУС ЗАМЕТКИ',
               'ДЕДЛАЙН']
    change = input('Выберите, что вы хотите изменить:\n'
          '\t1. Имя пользователя\n'
          '\t2. Заголовки\n'
          '\t3. Описание\n'
          '\t4. Статус заметки\n'
          '\t5. Дедлайн\n'
          'Введите номер пункта или пункт целиком: ')
    change = check_answer(changes, change)
    if change.upper() in ['1', 'ПОЛЬЗОВАТЕЛЬ']:
        new_username = input('Введите новое имя пользователя: ')
        note['username'] = new_username
        print(f'Имя пользователя изменено на {new_username.upper()}')
    elif change.upper() in ['2', 'ЗАГОЛОВКИ']:
        add_titles(note)
    elif change.upper() in ['3', 'ОПИСАНИЕ']:
        note['content'] = input('Введите новое описание заметки: ')
    elif change.upper() in ['4', 'СТАТУС ЗАМЕТКИ']:
        set_status(note)
    elif change.upper() in ['5', 'ДЕДЛАЙН']:
        set_issue_date(note)

# Проверка корректности ввода данных
def check_answer(answer_list, answer):
    while answer.upper() not in answer_list:
        answer = input('Введено некорректное значение, повторите ввод: ')
    return answer

# Функция подписи дней
def days_write(days):
    if 11 <= days % 100 <= 19:
        return 'дней'
    elif 2 <= days % 10 <= 4:
        return 'дня'
    elif days % 10== 1:
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
            return True
        except ValueError:
            print('Неверно введённый формат даты, повторите ввод')
            return False

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
        print(f'\t- Дедлайн был {abs(deadline_delta)} {days_write(deadline_delta)} назад!')

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

# Функция замены статуса
def set_status(note):
    answer = input("Хотите изменить статус заметки? (Да/Нет): ")
    while answer.upper() != "НЕТ":
        answer = check_answer(answer_list=['ДА', 'НЕТ'], answer=answer)
        if answer.upper() == 'НЕТ':
            break
        else:
            statuses = ['1', '2', '3', 'ВЫПОЛНЕНО', 'ОТЛОЖЕНО', 'В ПРОЦЕССЕ']
            status = input(f'Введите номер статус или наберите его текстом:\n'
                           f'\t{statuses[0]}: {statuses[3].upper()}\n'
                           f'\t{statuses[1]}: {statuses[4].upper()}\n'
                           f'\t{statuses[2]}: {statuses[5].upper()}\n')
            status = check_answer(statuses, status)
            if status.isdigit():
                status = statuses[int(status) + 2]
            note['status'] = status
            print(f'Статус заметки изменён на {status.upper()}')
            note['status'] = status
        answer = input("Хотите изменить статус заметки? (Да/Нет): ")

# Вывод информации
def get_info(note):
    for key, value in note.items():
        if key != 'titles':
            print(f"\t{key.capitalize()}: {value}")
    print("\tЗаголовки заметки:")
    for title in note['titles']:
        print("\t- ", title)
    print("\tДедлайн:")
    check_deadline(note)

def create_note():
    new_note = {}
    set_info(new_note)
    new_note['created_date'] = datetime.date.today()
    add_titles(new_note)
    while not set_issue_date(new_note):
        print('Дата введена некорректно, повторите ввод')
    set_status(new_note)
    return new_note

def save_note(new_note):
    global note_saver, note_id
    answer_for_save = input('Хотите сохранить заметку? (Да/Нет): ')
    answer_for_save = check_answer(['ДА', 'НЕТ'], answer_for_save)
    if answer_for_save.upper() == 'ДА':
        if new_note in note_saver.values():
            answer_for_save = input('Такая заметка уже есть. Вы точно хотите её сохранить? (Да/Нет): ')
            if answer_for_save.upper() == 'ДА':
                note_saver[str(note_id)] = new_note
                note_id += 1
                print('Вы сохранили ПОВТОРЯЮЩУЮСЯ заметку')
            else:
                print('Повторяющаяся заметка не была удалена')
        else:
            note_saver[str(note_id)] = new_note
            note_id += 1
            print('Новая заметка сохранена успешно')
    else:
        answer_for_save = input('Вы точно не хотите сохранять заметку? (Да/Нет): ')
        if answer_for_save.upper() == 'НЕТ':
            note_saver[str(note_id)] = new_note
            note_id += 1
            print('Новая заметка успешно сохранена')
        else:
            print('Заметка не была сохранена')

# Функция вывода заметок
def display_notes(note_dict):
    for ID, note in note_dict.items():
        print(f'Заметка #{ID}')
        get_info(note)
        print('-' * 20)
    if not note_dict:
        print('У вас нет сохранённых заметок')

# Функция удаления заметки
def delete_note():
    global note_saver
    if not note_saver:
        print('Список заметок пуст, удалять нечего')
        return
    delete_list_id = []
    answer_for_delete = input('Выберите критерий, по которому будете производить удаление\n'
                              '\t1. Пользователь\n'
                              '\t2. Заголовок\n'
                              'Введите номер пункта или критерий удаления текстом: ')
    answer_for_delete = check_answer(['1', '2', 'ПОЛЬЗОВАТЕЛЬ', 'ЗАГОЛОВОК'], answer_for_delete)
    if answer_for_delete.upper() in ['1', 'ПОЛЬЗОВАТЕЛЬ']:
        username = input('Введите имя пользователя, заметки которого хотите удалить: ')
        for ID, note in note_saver.items():
            if note['username'] == username:
                delete_list_id.append(ID)
        if delete_list_id:
            for ID in delete_list_id:
                del note_saver[ID]
            print(f'Все заметки с именем {username} были удалены')
            print('Список оставшихся заметок:')
            display_notes(note_saver)
        else:
            print(f'Нет заметок с именем {username}')
    else:
        title = input('Введите заголовок заметки(-ок), которую(-ые) хотите удалить: ')
        for ID, note in note_saver.items():
            if title in note['titles']:
                delete_list_id.append(ID)
        if delete_list_id:
            for ID in delete_list_id:
                del note_saver[ID]
            print(f'Все заметки с заголовком {title} были удалены')
            print('Список оставшихся заметок:')
            display_notes(note_saver)
        else:
            print(f'Нет заметок с заголовком {title}')

# Функция поиска заметки
def search_notes(notes, keyword=None, status=None):
    search_dict = {}
    if not note_saver:
        print('Список заметок пуст, искать нечего')
        return
    for ID, note in notes.items():
        search_list = str(note.values())
        if keyword and status:
            if (keyword in search_list) and (note['status'] == status):
                search_dict[ID] = note
        elif keyword:
            if keyword in search_list:
                search_dict[ID] = note
        elif status:
            if note['status'] == status:
                search_dict[ID] = note
        else:
            print('Ничего не нашлось')
            break
    print(f"По вашему запросу {keyword} и {status}: {len(search_dict)}")
    display_notes(search_dict)

# Функция записи списка заметок в файл
def save_notes_to_file(notes, filename):
    f = open(filename, 'w', encoding='UTF-8')
    for ID, note in notes.items():
        f.write(f'Заметка #{ID}\n')
        for key, value in note.items():
            if key != 'titles':
                f.write(f'{key.capitalize()}: {value}\n')
            else:
                f.write(f'{key.capitalize()}:\n')
                for title in note['titles']:
                    f.write(f'\t- {title}\n')
        f.write('-'*15 + '\n')
    f.close()


# Функция цикличного меню с выбором действий
def menu():
    while True:
        action_list = ['1', '2', '3', '4', '5', '6',
                       'СОЗДАТЬ НОВУЮ ЗАМЕТКУ',
                       'ПОСМОТРЕТЬ ВСЕ ЗАМЕТКИ',
                       'ОБНОВИТЬ ЗАМЕТКИ',
                       'УДАЛИТЬ ЗАМЕТКУ',
                       'НАЙТИ ЗАМЕТКИ',
                       'ВЫХОД']
        action = input('Возможные действия:\n'
                       '\t1. Создать новую заметку\n'
                       '\t2. Посмотреть все заметки\n'
                       '\t3. Обновить заметку\n'
                       '\t4. Удалить заметку\n'
                       '\t5. Найти заметки\n'
                       '\t6. Выход\n'
                       'Впишите номер действия или действие целиком и нажмите "Enter": ')
        action = check_answer(action_list, action).upper()
        if action in ['1', 'СОЗДАТЬ НОВУЮ ЗАМЕТКУ']:
            note = create_note()
            save_note(note)
        elif action in ['2', 'ПОСМОТРЕТЬ ВСЕ ЗАМЕТКИ']:
            display_notes(note_saver)
        elif action in ['3', 'ОБНОВИТЬ ЗАМЕТКИ']:
            update_note()
        elif action in ['4', 'УДАЛИТЬ ЗАМЕТКУ']:
            delete_note()
        elif action in ['5', 'НАЙТИ ЗАМЕТКИ']:
            key = input('Введите ключевое слово для поиска: ')
            stat = input('Введите статус заметки для поиска: ')
            search_notes(note_saver, key, stat)
        else:
            print('Завершение работы программы')
            break
    print('До свидания!')


'''ОСНОВНОЙ БЛОК КОДА'''

menu()
save_notes_to_file(note_saver, 'notesaver.txt')
