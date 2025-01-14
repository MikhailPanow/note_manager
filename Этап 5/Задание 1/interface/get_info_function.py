'''

Вывод информации

  Функция предназначена для предоставления информации пользователю о заметке, которую в качестве параметра принимает
функция
'''


def get_info(note):
    for key, value in note.items():
        if key != 'titles':
            print(f"\t{key.capitalize()}: {value}")
    print("\tЗаголовки заметки:")
    for title in note['titles']:
        print("\t- ", title)
    print("\tДедлайн:")
    check_deadline(note)