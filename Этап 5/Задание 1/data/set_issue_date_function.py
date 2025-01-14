'''
Функция ввода даты от пользователя в корректном виде

  Функция предназначена для ввода даты дедлайна в заметку в 2-х форматах:
    - ГГГГ-ММ-ДД
    - ДД-ММ-ГГГГ

  При верном вводе функция возвращает True и записывает дату дедлайна в заметку,
иначе - False и выводит на консоль сообщение: "Неверно введенный формат даты, повторите ввод"

  Реализовано с помощью библиотеки datetime и конструкции try-except. Ошибка: ValueError
'''


def set_issue_date(note):
    issue_date = input('Введите дату истечения заметки в формате ГГГГ-ММ-ДД или ДД-ММ-ГГГГ: ')
    try:
        issue_date = datetime.datetime.strptime(issue_date, '%d-%m-%Y').date()
        note['issue_date'] = issue_date.strftime('%d-%m-%Y')
        return True
    except ValueError:
        try:
            issue_date = datetime.datetime.strptime(issue_date, '%Y-%m-%d').date()
            note['issue_date'] = issue_date.strftime('%Y-%m-%d')
            return True
        except ValueError:
            print('Неверно введённый формат даты, повторите ввод')
            return False