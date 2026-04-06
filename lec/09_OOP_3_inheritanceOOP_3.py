# Реалізація принципів ООП: 
# інкапсуляція (приховування даних (атрибутів, полів) екземпляоа класу), 
# наслідування
# поліморфізм (перевизначення методів класу),

# ДОСТУП ДО ПОЛІВ ЧЕРЕЗ ВЛАСТИВОСТІ
#================НАСЛІДУВАННЯ===================
# defination
class Human():
    # атрибути класу:
    infoHuman="You are human!!!"
    countHuman=0
    #properties, fields, attr =>атрибути екземпляра класу в конструкторі => обєкт
    def __init__(self,name="Noname",age=1):
        """ Ініціалізація атрибутів екземпляру name, age"""
        # приховані атрибути => private => доступний в класі
        self.__name=name
        self.__age=age
        Human.countHuman+=1
    
    # getter, setter => декоратори @property
    @property
    def age(self):
        return self.__age
    
    # setter => @[propyrty].setter
    @age.setter
    def age(self, age):
        if 1<age<120:
            self.__age=age
        else:
            print("Error AGE (1;120)")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def set_name(self,name):
        if name!=None or name!="":
            self.__name=name
    
    #методи класу => def
    def say_something(self,words):
        print(f"Human {self.__name} say: '{words}'")
    
    def print_info(self)->None:
        print(f"Human => {self.__name} has {self.age} years old")
   
    # рядкове представлення обєкта Human
    def __str__(self) -> str:
        return f'Human: {self.__name}, {self.__age} years old'



class Student(Human):
    """Клас Student"""
    def __init__(self, name, age, number_gradebook, group):
        super().__init__(name,age)
        # Human.__init__(name, age)
        self.__number_gradebook=number_gradebook
        self.__group=group

    @property
    def number_gradebook(self):
        return self.__number_gradebook
    
    @number_gradebook.setter
    def set_number_gradebook(self,number_gradebook):
        self.__number_gradebook=number_gradebook
    
    @property
    def group(self):
        return self.__group
    
    @group.setter
    def group(self,group):
        self.__group=group

    def print_info(self)->None:
        # print(f"Human {super().name} has {super().age} yeas old")
        super().print_info()
        print(f"Group: {self.__group}. GradeBook # {self.__number_gradebook}")
    
    def __str__(self) -> str:
        return super().__str__()+f" (Group: {self.__group}. GradeBook #{self.__number_gradebook})"

# # ===============using class===============
human1=Human()
human2=Human("Olga",18)
print(human1)
print(human2)
print(human1.age)
print(human2.age)
human2.age=20
print(human2.age)
human1.age=-10
human1.age=200
# human2.print_info()

student1=Student("Роман",18,"123/23-01","ЦТ-21")
student2=Student("Аліна",18,"123/23-02","ІСТ-31")
student3=Student("Дмитро",19,"123/23-03","ЦТ-11(3р.н.)")
student1.group="ІСТ-31"
student1.print_info()
print(student1.name)
# student1.print_info()
print(student1)
print(student2)
print(student3)