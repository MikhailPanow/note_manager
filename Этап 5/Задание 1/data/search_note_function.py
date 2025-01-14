'''
Функция поиска заметки

  Предназначена для поиска заметок в списке сохраненных заметок во всех полях и отображения их на консоли
'''
def search_notes(notes, keyword=None, status=None):
    search_dict = {}
    if not note_saver:
        print('Список заметок пуст, искать нечего')
        return
    for ID, note in notes.items():
        search_list = str(note.values())
        if keyword and status:
            if (keyword in search_list) and (note['status'] == status):
                search_dict[ID] = note
        elif keyword:
            if keyword in search_list:
                search_dict[ID] = note
        elif status:
            if note['status'] == status:
                search_dict[ID] = note
        else:
            print('Ничего не нашлось')
            break
    print(f"По вашему запросу {keyword} и {status}: {len(search_dict)}")
    display_notes(search_dict)
