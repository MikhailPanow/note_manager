'''
Функция для запроса данных от пользователя

  Функция предназначена для запроса информации от пользователя не требующей проверки и ввода ее в заметку
'''


def set_info(note):
    note['username'] = input("Введите имя пользователя: ")
    note['content'] = input("Введите описание заметки: ")
    return note