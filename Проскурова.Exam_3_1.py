# 1. Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код.
# После этого выводит на экран номер карты с первыми четырьмя цифрами, остальные заменены на звездочки,
# CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

def bank(number_cart, cvc_cod, pin_cod):
    print(f"Ваша карта:{number_cart[:4]}{'*'*(len(number_cart)-4)}")
    print(f"CVC-код: {'#'*len(cvc_cod)}")
    print(f"PIN-код: {'&'*(len(pin_cod)-1)}{pin_cod[-1]}")


bank(number_cart=input("Введите номер карты:"), cvc_cod=input("Введите CVC-код:"), pin_cod=input("Введите PIN-код:"))