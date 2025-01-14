'''
Функция сохранения данных в файл json

  Функция структурированно сохраняет данные в файл с расширением json
'''
def save_notes_json(notes, filename):
    with open(filename, 'w', encoding='UTF-8') as json_f:
        json_f.write(json.dumps(notes, ensure_ascii=False, indent=4))