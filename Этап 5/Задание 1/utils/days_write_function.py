'''
Функция написания дней

  Функция используется для корректного вывода слова "день" в соответствующей числительному форме

  Функция принимает количество дней, с которым употребляется слово "день". В зависимости от введенного
числа функция возвращает слово с верным окончанием для дальнейшего вывода
'''


def days_write(days):
    if 11 <= days % 100 <= 19:
        return 'дней'
    elif 2 <= days % 10 <= 4:
        return 'дня'
    elif days % 10== 1:
        return 'день'
    else:
        return 'дней'