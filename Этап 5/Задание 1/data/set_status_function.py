'''
Функция замены статуса

  Функция предназначена для цикличного запроса изменения статуса у пользователя
'''
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