from math import sin, pow, sqrt
# defination function
#function without parameters 
def hello():
    print("Hello, world!")

hello()
hello()
hello()
hello()


# print(print("Hello"))
# print(hello())

# #with parametres
def hello_by_name(username):
    print(f"Hello, {username}!")

hello_by_name("Tata")
print(hello_by_name)
print(type(hello_by_name))
myhello=hello_by_name

myhello("Tetiana")

def suma(a:int,b:int)->None:
    """
    @a parametr
    @b parametr
    @a+@b output suma 
    """
    print(f"{a}+{b}={a+b}")

suma(2,3)    
suma(2,7)    
suma(8,7) 
suma(b=88,a=77) 
my_suma=suma 
my_suma(33.3,77.7)


def multiply(a=0,b=0)-> int:
    """
    Multiply a*b
    """
    result=a*b #local variable
    return result

dobutok=multiply(3,4)
print(dobutok)
print(multiply(4,5))

# #(4*5+7*8)*9

viraz=multiply(multiply(4,5)+multiply(7,8),9)
print(viraz)

# #using parameters by default
def info_student(firstname,secondname,age=18):
    print(f"{firstname} {secondname} has {age} years old.")

info_student("Mikola","Gerelchuk",18)
# #using nameof parametres
info_student(age=23,firstname="First1",secondname="Second1")
info_student("Віталій","Фінчук")


# # #==================
def get_sum(*nums):
    print(type(nums))
    print(nums)
    s = 0 #local variable
    for a in nums:
        s += a
    print(locals())
    return s

print(get_sum(1, 2, 5, 6, 7))
seq_number=[4,5,6,11,22]
print(get_sum(*seq_number)) # <=> get_sum(4,5,6,11,22)
# print(get_sum(seq_number))

def arg(*args):
    for arg in args:
        print(arg)
        
arg(1, 2, 3, "Python")

def marks_by_student(name,*marks):
    print(f"Student {name} has marks: ", end="")
    for mark in marks:
        print(mark, end="; ")

marks_by_student("Mikola",4,5,4,5,4,4)
print("="*48)

# # # ===============**kwargs==========
capital_of_country={"Ukraine":"Kiyv","Poland":"Warshawa"} #global variable

def info_capital(**capital): #{"Ukraine":"Kiyv","Poland":"Warshawa"}
    print(capital)

info_capital(Ukraine="kiyv", Poland="Warshawa")
info_capital(**capital_of_country)

# print("*"*50)
# print(globals())
print("*"*50)
# print(locals())

count_student_in_ct2=12 #global variable
def working_with_group(group,append_student):
    """
    Збільшення кількості студентів в групі
    group
        група
    append_student 
        кількість студентів
    """
    # область видимості функції
    # global count_student_in_ct2
    count_student_in_ct2=0 #local 
    count_student_in_ct2+=append_student
    print(f"{group} has count (in func) students: {count_student_in_ct2}")


working_with_group("CT-31",4)
print(f"Out value count students: {count_student_in_ct2}")
# # ==============name function as params function===
def expression_calc(a,b,func:function):
    if func==add:
        print(func(a,b)**2)
    else:
        print(func(a,b))

def add(a,b):
    return a+b

def div(a,b):
    if b==0:
        b=1
    return a/b

def kw_minues(a,b):
    return (a+b)*(a-b)


expression_calc(4,5,add)
expression_calc(4,5,div)
expression_calc(4,5,kw_minues)

print(eval("4+6*7/8"))

# x=10
def expression_calc2(a,b,func):
    x=0 #local
    x+=12
    if func==add:
        def suma_kub():
            nonlocal x
            # global x
            x+=2
            y=8
            return (x+y)**3
        return func(a,b)**2+suma_kub()
    return func(a,b)

print(expression_calc2(3,5,add))

expression1=lambda x,y:  sqrt(sin(x)+pow(y,4))
print(expression1(3,5))
print(f"{expression_calc2(3,5,expression1):<10.4f}!!!")
