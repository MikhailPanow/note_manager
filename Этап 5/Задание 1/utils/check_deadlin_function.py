import datetime

'''
Функция проверки дедлайна

  Функция предназначена для определения количества дней до дедлайн
  
  В качестве параметра функция принимает заметку с заранее записанной датой для сравнения с датой просмотра заметки
и выводит на консоль соответствующие сообщения
'''

def check_deadline(note):
    try:
        issue_date = datetime.datetime.strptime(note['issue_date'], '%Y-%m-%d')
    except ValueError:
        issue_date = datetime.datetime.strptime(note['issue_date'], '%d-%m-%Y')
    created_date = datetime.datetime.now()
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