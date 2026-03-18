def info_user(login, email, age): #параметри
    print(f"Info user:\nlogin: {login}\nemail: {email}\nage: {age}")

# #використання параметрів за замовчуванням => порядок виклику аргументів функції не має значенн
def info_user1(login, email, age=30):
    print(f"Info user:\nlogin: {login}\nemail: {email}\nage: {age}")


def info_user2(login,email, age=None): #None => NoneType
    print(f"Info user:\nlogin: {login}\nemail: {email}\nage: {age}")


def multiply(a=0,b=0)-> int:
    """
    Multiply a*b
    """
    result=a*b #local variable
    return result

if "__name__"=="__main__":
    pass