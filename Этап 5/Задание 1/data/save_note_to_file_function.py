'''
Функция записи списка заметок в файл

  Функция сохраняет данные сохраненных в программе заметок в файл

  При ошибках файла выводятся соответствующие сообщения

'''
def save_notes_to_file(notes, filename):
    try:
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
            f.write('-'*20 + '\n')
        f.close()
    except FileNotFoundError:
        print('Файла с таким именем не существует. Проверьте наличие файла или проверьте корректность ввода данных')
    except UnicodeError:
        print('Этот файл написан в другой кодировки - нет возможности для расшифровки')