'''
Функция загрузки из файла

  Функция выгружает данные по заметкам из файла в переменную программы

  При ошибке файла выводятся соответствующие сообщения
'''


def load_from_file(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            for info in f:
                if 'Заметка' in info:
                    number = info[9:-1]
                    note_saver[str(number)] = {}
                if 'Username' in info:
                    note_saver[str(number)]['username'] = info[10:-1]
                if 'Content' in info:
                    note_saver[str(number)]['content'] = info[9:-1]
                if 'Created_date' in info:
                    note_saver[str(number)]['created_date'] = info[14:-1]
                if 'Titles' in info:
                    title_list = []
                    info = f.readline()
                    while '\t-' in info:
                        title_list.append(info[3:-1])
                        info = f.readline()
                    note_saver[str(number)]['titles'] = title_list
                if 'Issue_date' in info:
                    note_saver[str(number)]['issue_date'] = info[12:-1]
                if 'Status' in info:
                    note_saver[str(number)]['status'] = info[8:-1]
    except FileNotFoundError:
        print('Файла с таким именем не существует. Проверьте наличие файла или проверьте корректность ввода данных')
    except UnicodeError:
        print('Этот файл написан в другой кодировки - нет возможности для расшифровки')