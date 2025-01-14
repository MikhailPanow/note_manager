'''
Функция удаления заметки

  Предназначена для удаления заметок по одному из параметров:
    - Пользователь
    - Заголовок

  Функция удаляет ВСЕ заметки, подходящие под соответствующие параметры
'''
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