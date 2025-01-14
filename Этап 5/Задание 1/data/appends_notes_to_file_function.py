'''
Функция добавления данных в файл

  Функция предназначена для добавления заметок в файл без удаления старых данных
'''


def append_notes_to_file(notes, filename):
    try:
        with open(filename, 'a', encoding='UTF-8') as f:
            for ID, note in notes.items():
                f.write(f'Заметка #{ID}\n')
                for key, value in note.items():
                    if key != 'titles':
                        f.write(f'{key.capitalize()}: {value}\n')
                    else:
                        f.write(f'{key.capitalize()}:\n')
                        for title in note['titles']:
                            f.write(f'\t- {title}\n')
                f.write('-' * 20 + '\n')
            f.close()
    except FileNotFoundError:
        with open(filename, 'x', encoding='UTF-8'):
            append_notes_to_file(notes, filename)
    except UnicodeError:
        print('Этот файл написан в другой кодировки - нет возможности для расшифровки')