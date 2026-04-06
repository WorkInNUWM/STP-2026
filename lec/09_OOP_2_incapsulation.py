# Реалізація принципів ООП: 
# 1) інкапсуляція (приховування даних (атрибутів, полів) екземпляоа класу), 
# 2) наслідування
# 3) поліморфізм (перевизначення методів класу),


#================Інкапсуляція===================
class Human:
    # атрибути класу:
    infoHuman="You are human!!!"
    countHuman=0
    #properties, fields, attr =>атрибути екземпляра класу в конструкторі => обєкт
    def __init__(self,name="Noname", age=20):
        """ Ініціалізація атрибутів екземпляру name, age"""
        # доступний => public  => доступний за межами класу
        self.name=name
        # прихований => private => доступний в класі
        self.__age=age
        # self._surname="Surname"
        Human.countHuman+=1
    
    # # getter, setter
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if 1<age<120:
            self.__age=age
        else:
            print("Error AGE (1;120)")

    #методи класу => def
    def say_something(self,words):
        print(f"Human {self.name} say: '{words}'")
    
    def print_info(self):
        print(f"Human {self.name} has {self.__age} yeas old")
   
    # рядкове представлення обєкта
    def __str__(self) -> str:
        return f'Human: {self.name}, {self.__age} year old'
    
    def __repr__(self) -> str:
        return f"Human({self.name},{self.age})"

human1=Human("Olga")
# print(human1.__age) #AttributeError: 'Human' object has no attribute '__age'
# print(human1._surname)
# human1._surname="Igor"
# print(human1._surname)
##human1.__age=12 #за межами класу
##print(human1.__age)
##print(human1)

print(human1.get_age())
human1.set_age(-3)
print(human1.get_age())
human1.set_age(21)
print(human1.get_age())

human1.say_something("Hello! How are you?")
human1.print_info()
print("Human1",human1.get_age(),"yeas old")
# human1.surname="Gala" #новий атрибут екземпляра, який створюється динамічно
# # # print(human1.surname)
# # # print(human1.__age) #error
# # # print(human1.infoHuman)
# # # print(Human.infoHuman)


# human2=Human(name="Dmitro", age=20)
# human2.print_info()
# human2.name="Dmitro"
# human2.age=21
# human2.print_info()
# human2.say_something("Hi! I am fine, thanks")
# # print(human2.name)
# # print(human2.infoHuman)
# # print(Human.infoHuman)


# print(f"Created object Human: {Human.countHuman}")
# listHuman=[human1, human2]
# print("Working list of humans:")
# for human in listHuman:
#     print(human)