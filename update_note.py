'''ИНИЦИАЛИЗАЦИЯ'''

# Подключение datetime для работы с датами
import datetime

# Глобальная переменная списка записок
note_saver = {}

# Глобальная переменная ID
note_id = 1

# Обновление заметки
def update_note(note):
    print('Текущие данные заметки: ')
    get_info(note)
    changes = ['1', '2', '3', '4', '5',
               'ИМЯ ПОЛЬЗОВАТЕЛЯ', 'ЗАГОЛОВКИ',
               'ОПИСАНИЕ', 'СТАТУС ЗАМЕТКИ',
               'ДЕДЛАЙН']
    change = input('Выберите, что вы хотите изменить:\n'
          '\t1. Имя пользователя'
          '\t2. Заголовки'
          '\t3. Описание'
          '\t4. Статус заметки'
          '\t5. Дедлайн'
          'Введите номер пункта или пункт целиком: ')
    check_answer(changes, change)
    if change.upper() in ['1', 'ПОЛЬЗОВАТЕЛЬ']:
        new_username = input('Введите новое имя пользователя: ')
        note['username'] = new_username
        print(f'Имя пользователя изменено на {new_username.upper()}')
    elif change.upper() in ['2', 'ЗАГОЛОВКИ']:
        add_titles(note)
    elif change.upper() in ['3', 'ОПИСАНИЕ']:
        note['content'] = input('Введите новое описание заметки: ')
    elif change.upper() in ['4', 'СТАТУС ЗАМЕТКИ']:
        change_status(note)
    elif change.upper() in ['5', 'ДЕДЛАЙН']:
        set_issue_date(note)

# Проверка корректности ввода данных
def check_answer(answer_list, answer):
    while answer.upper() not in answer_list:
        answer = input('Введено некорректное значение, повторите ввод:')

# Функция подписи дней
def days_write(days):
    if len(days) >= 2:
        if 11 <= int(days[-2:]) <= 19:
            return 'дней'
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
def first_status(note):
    statuses = ['1', '2', '3', 'ВЫПОЛНЕНО', 'ОТЛОЖЕНО', 'В ПРОЦЕССЕ']
    status = input(f'Введите номер статус или наберите его текстом:\n'
                   f'\t{statuses[0]}: {statuses[3].upper()}\n'
                   f'\t{statuses[1]}: {statuses[4].upper()}\n'
                   f'\t{statuses[2]}: {statuses[5].upper()}\n')
    check_answer(statuses, status)
    if status.isdigit():
        status = statuses[int(status) + 2]
    note['status'] = status
    print(f'Статус заметки изменён на {status.upper()}')
    return note

# Функция замены статуса
def change_status(note):
    status = note['status']
    answer = input("Хотите изменить статус заметки? (Да/Нет): ")
    while answer.upper() != "НЕТ":
        check_answer(answer_list=['ДА', 'НЕТ'], answer=answer)
        if answer.upper() == 'НЕТ':
            print(f'Вы решили не изменять статус {status.upper()}')
        else:
            first_status(note)
        answer = input("Хотите изменить статус заметки? (Да/Нет): ")
    note['status'] = status

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
    return new_note

def save_note(new_note):
    global note_saver, note_id
    answer_for_save = input('Хотите сохранить заметку? (Да/Нет): ')
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
def get_notes():
    global note_saver
    for ID, note in note_saver.items():
        print(f'Заметка #{ID}')
        get_info(note)

# Функция удаления заметки
def delete_note():
    global note_saver
    delete_list_id = []
    answer_for_delete = input('Выберите критерий, по которому будете производить удаление\n'
                              '\t1. Пользователь\n'
                              '\t2. Заголовок\n'
                              'Введите номер пункта или критерий удаления текстом: ')
    check_answer(['1', '2', 'ПОЛЬЗОВАТЕЛЬ', 'ЗАГОЛОВОК'], answer_for_delete)
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
            get_notes()
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
            get_notes()
        else:
            print(f'Нет заметок с заголовком {title}')


'''ОСНОВНОЙ БЛОК КОДА'''

print('Добро пожаловать в менеджер заметок!\n')
answer_for_create = input('Хотите создать новую заметку? (Да/Нет): ')
while answer_for_create.upper() != "НЕТ":
    check_answer(['ДА', 'НЕТ'], answer_for_create)
    if answer_for_create.upper() == 'НЕТ':
        break
    else:
        some_note = create_note()
        save_note(some_note)
    answer_for_remove = input('Хотите ли вы удалить какую-нибудь заметку? (Да/Нет): ')
    check_answer(['ДА', 'НЕТ'], answer_for_remove)
    if answer_for_remove.upper() == 'ДА':
        delete_note()
        print('Список сохраненных заметок:')
        get_notes()
    answer_for_info = input('Хотите просмотреть заметки? (Да/Нет): ')
    check_answer(['ДА', 'НЕТ'], answer_for_info)
    if answer_for_info.upper() == 'ДА':
        print('Список сохраненных заметок:')
        get_notes()
    answer_for_create = input('Хотите создать новую заметку? (Да/Нет): ')
print('До новых встреч!')