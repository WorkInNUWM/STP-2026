# def info_user(login, email, age): #параметри
#     print(f"Info user:\nlogin: {login}\nemail: {email}\nage: {age}")


# #використання позиціювання аргументів   
# # info_user("TSShrol","tetiana.shrol@rshu.edu.ua",43)
# # # info_user("TSShrol","tetiana.shrol@rshu.edu.ua") #TypeError=> error

# # # #використання іменованих аргументів => порядок виклику аргументів функції не має значенн
# # info_user(login="TSShrol",email="tetiana.shrol@rshu.edu.ua",age=43)
# # info_user(login="TSShrol",age=43,email="tetiana.shrol@rshu.edu.ua")


# # #використання параметрів за замовчуванням => порядок виклику аргументів функції не має значенн
# def info_user1(login, email, age=30):
#     print(f"Info user:\nlogin: {login}\nemail: {email}\nage: {age}")

# # info_user1(login="TSShrol",email="tetiana.shrol@rshu.edu.ua") #  age=30
# # info_user1(login="TSShrol",email="tetiana.shrol@rshu.edu.ua",age=38) # age=38
# # info_user1("TSShrol","tetiana.shrol@rshu.edu.ua",43)

# def info_user2(login,email, age=None): #None => NoneType
#     print(f"Info user:\nlogin: {login}\nemail: {email}\nage: {age}")

# # info_user2("TSShrol","tetiana.shrol@rshu.edu.ua")
# # print(info_user2("TSShrol","tetiana.shrol@rshu.edu.ua")) #None


# def suma_number(*numbers):
#     s=0
#     for number in numbers:
#         s+=number
#     return s

# # result=suma_number(1,2,3,4,5)
# # print(result)
# # print(suma_number(4,5,6))
# # result=suma_number(*[1,2,3,4,5])
# # print(result)

# # #Напишіть програму, яка отримує три цілих числа, введені 
# # # з клавіатури (кожне число вводиться на окремому рядку),
# # #  і друкує на екрані їх суму, добуток, результат 
# # # піднесення першого числа до степеня різниці другого і третього чисел.
# # """
# def sumN(n1,n2,n3):
#     return n1+n2+n3

# def multiplyN(n1,n2,n3):
#     return n1*n2*n3

# def powN(n1,n2,n3):
#     return n1**(n2-n3)


# def runtask():
#     n1=int(input("Input n1: "))
#     n2=int(input("Input n2: "))
#     n3=int(input("Input n3: "))
#     print(f"suma={sumN(n1,n2,n3)}\nmultiply={multiplyN(n1,n2,n3)}\npow={powN(n1,n2,n3)}")

# runtask()
# runtask()
# runtask()

# print(sum(range(1,101)))

def print_list(items_list=[]):
    print("[",end="")
    for item in items_list:
        if item==items_list[-1]:
            print(item, end="")
        else:
            print(item,end=";")
    print("]")

print_list([4,5,6,7])

# змінюється вхідний список
def append_list(items_list=[]):
    print(id(items_list))
    items_list.append(1)

l=[]
print(id(l))
append_list(l)
print(l)
append_list(l)
print(l)
append_list(l)
print(l)

#створення нового списку
def append_list_1(items_list=[]):
    print(id(items_list))
    new_list=list(items_list)
    print(id(new_list))
    new_list.append(1)
    return new_list




print(append_list_1(l))
print(l)
print(append_list_1(l))
print(l)
print(append_list_1(l))
print(l)


# # #функції із параметрами *
# def suma_number_flag(flag=True,*nums):
#     """
#     Повертає суму парних чисел, якщо flag=True;
#     повертає суму непарних чисел, якщо flag=False;
#     """
#     print(flag,nums)
#     suma_num=0
#     for item in nums:
#         if flag==True and item%2==0: #parne
#             suma_num+=item
#         elif flag==False and item%2==1: #neparne
#             suma_num+=item
#     return suma_num

# print(suma_number_flag(True,3,4,5,6,7))
# print(suma_number_flag(False,3,4,5,6,7))
# print(suma_number_flag(1, *[3,4,5,6,7]))
# print(suma_number_flag.__doc__)
# if "f":
#     print("True")
# else:
#     print("False")

# # #функції із параметрами **
# # def func_library(**books):
# #     print(type(books))
# #     # print(books)
# #     for author, book in books.items():
# #         print(author," написав(-ла) ", book)

    

# # #варіанти виклику функції
# # func_library(**{"Франко":["Каменярі","Борислав сміється"],"Шевченко":["Катерина","Заповіт"]})
# # library={"Франко":["Каменярі","Борислав сміється"],"Шевченко":["Катерина","Заповіт"]}
# # func_library(**library)
# # func_library(Українка=["Лісова пісня","Contra Spem Spero"])


# x=10
# def change():
#     # x=0
#     global x
#     x=x+5
#     print("inner x=",x)


# change()
# print("outer x=",x)