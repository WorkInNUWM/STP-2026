# try: #блок, де може виникнути помилка
#     number = int(input("Введіть число: "))
#     print("Введене число:", number)
# except: #перехоплення та обробка всіх винятків
#     print("Перетворення прошло невдало")

# print("Продовження програми")


# try: #блок, де може виникнути помилка
#     number = int(input("Введіть число: "))
#     print("Введене число:", number)
#     print("Введене число:", number/str(number))

# except TypeError as e: #перехоплення та обробка всіх винятків
#     print("Перетворення прошло невдало",e)
# except ValueError:
#     print("Введені дані не є числом!!!!!",ValueError.__doc__)
# else:
#     print("Блок коду виконався без помилок")
# finally:
#     print("Я виконуюсь завжди. Тут можете звільнити ресурси (закрити файл, закрити зєднання з БД )")

# print("Продовження програми")

# try :   фрагмент коду, в якому може бути виянток!!!
# except тип_виключення(помилка):: коли є виняток !!!
# else:  нема винятку
# finaly:    завжди виконується


# list1=[3,45]
# try: #блок, де може виникнути помилка
#     number1 = int(input("Введіть число: "))
#     number2 = int(input("Введіть число: "))
#     # if number2==0:
#     #     raise Exception(f"{number1}/{number2} - ділення на нуль ")
#     print("Введене число:", number1/number2)
#     # print(list1[2]) #IndexError => Exception
# except TypeError as e: #перехоплення та обробка всіх винятків
#     print("Перетворення прошло невдало",e)
# except ValueError as e:
#     print(e)
#     print("input int number")
# except ZeroDivisionError as e:
#     print(e.__doc__)
# except Exception as e:
#     print("name Exception: ",e)
# else:
#     print("Блок коду виконався без помилок")
# finally:
#     print("Я виконуюсь завжди. Тут можете звільнити ресурси (закрити файл, закрити зєднання з БД )")


try:
    print(xxx)
except NameError:
    pass
    # print("xxx -  not defined")