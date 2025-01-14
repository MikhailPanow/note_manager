'''
Функция вывода сохраненных заметок

  Функция выводит информацию из словаря заметок (выводятся сохраненные заметки на момент работы программы)
'''
def display_notes(note_dict):
    for ID, note in note_dict.items():
        print(f'Заметка #{ID}')
        get_info(note)
        print('-' * 20)
    if not note_dict:
        print('У вас нет сохранённых заметок')