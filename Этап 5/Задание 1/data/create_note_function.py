'''
Функция создания заметки

  Предназначена для создания заметки с данными, введенными от пользователя
'''

def create_note():
    new_note = {}
    set_info(new_note)
    new_note['created_date'] = datetime.date.today().strftime('%Y-%m-%d')
    add_titles(new_note)
    while not set_issue_date(new_note):
        print('Дата введена некорректно, повторите ввод')
    set_status(new_note)
    return new_note