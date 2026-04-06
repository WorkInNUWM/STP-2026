# Вступ в ООП
# ============визначення класу=======
# from typing import overload
class Human:
    """Клас Людина"""
    # змінні (атрибути) класу
    count_human=0
    info_human="You are human!!!"
    
    #properties, fields, attr => атрибути екземпляра класу
    # def __init__(self):
    #     self.name="Olga"
    #     self.age=20
   
    # конструктор
    def __init__(self, name="Olga", age=20):
        self.name=name
        self.age=age
        Human.count_human+=1
        print(f"Created new human #{Human.count_human}!")

    # деструктор
    def __del__(self):
        Human.count_human-=1
        print(f"Last {Human.count_human} humans!")

    # # метод класу
    def print_info_class():
        print(f"INFO => {Human.count_human} {Human.info_human}")
    
    # # метод екземпляра класу
    def print_info(self):
        print(f"human => {self.name} {self.age}")

    def say_something(self,words="Hello"):
        print(f'{self.name} say: "{words}" ')

    # # рядкове представлення обєкта для використання фунцією print
    def __str__(self):
        return f"Human {self.name} has {self.age} yeas old!"

    # # рядкове представлення обєкта, що використовуються для create by function repr
    
    def __repr__(self) :
        return f"Human('{self.name}',{self.age})"

# # =============використання класу==========
if __name__=="__main__":      
    human1 = Human()
    print(human1)
    # print(human1.info_human)
    # print(human1.name)
    # print(Human.count_human)

    human2= Human()
    print(human2)
    # print(human2.info_human)
    # print(human2.name)
    human2.name="Mihajlo"
    # print(human2.name)
    human2.age=21
    # print(human2.age)
    print(human2)
    # print(human1)
    # print(f"Human: {human2.name} has {human2.age} years old...!!!")
    # # Human.count_human+=1
    # print(human1.count_human) # не бажаний спосіб
    # print(human2.count_human) # не бажаний спосіб
    # print(Human.count_human) #бажаний спосіб
    # human1.count_human=7
    # print(human1.count_human)
    # print(human2.count_human)
    # print(Human.count_human)
    # # ============================
    # print(f"human1 => {human1.name} {human1.age}")
    # human2.age=21
    # human2.name="Oksana"
    # print(f"human2 => {human2.name} {human2.age}")
    
    # # ============ виклик конструктора з аргументами =========
    human3=Human("Marina",22)
    human4=Human(age=21,name="Дмитро")
    print(f"human3 => {human3.name} {human3.age}")
    print(f"human4 => {human4.name} {human4.age}")
    print(human3) # without __str__  =>  <__main__.Human object at 0x00000xxxxxxxxxxx>
    print(human4) # without __str__  =>  <__main__.Human object at 0x00000xxxxxxxxxxx>


    # Human.print_info_class() #without self
    ## human1.print_info_class() #TypeError: Human.print_info_class() takes 0 positional arguments but 1 was given
    human1.print_info()
    human2.print_info()
    human3.print_info()
    human4.print_info()

    # # without __repr__ [<__main__.Human object at 0x000001AECEE31160>, <__main__.Human object at 0x000001AECEDB5090>, <__main__.Human object at 0x000001AECEDB5F90>, <__main__.Human object at 0x000001AECEBAB100>]
    group_humans=[human1,human2, human3, human4] 
    print(group_humans)

    # # with __repr__ 
    print("Виведення інформації про людей із group_humans:")
    for human in group_humans:
        print(human)

    # # deleted obj
    del human3 
    for _ in range(4):
        print("Code...")
    
    # human2.__del__()
    human_with_repr=repr(human1) #new object
    print(id(human_with_repr))
    print(id(human1))

    human4.say_something()
    human2.say_something("Hi, how are you")
    human4.say_something("Hi!!!")
    human1.say_something("So-so!")
    # # NameError: name 'human3' is not defined. Did you mean: 'human1'?
    # # human3.say_something("I am fine!") 
    human1.say_something()