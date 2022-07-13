# 2. Напишите функцию, которая возвращает True,
# если введенный текст читается одинаково слева-направо и справа-налево. Иначе – False.

def func1(txt):
    if txt[::1] == txt[::-1]: print('True')
    else: print('False')


func1("gggssggg")