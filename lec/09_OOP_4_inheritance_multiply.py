# Реалізація принципів ООП: 
# інкапсуляція (приховування даних (атрибутів, полів) екземпляоа класу), 
# наслідування
# поліморфізм (перевизначення методів класу),

# ДОСТУП ДО ПОЛІВ ЧЕРЕЗ МЕТОДИ get, set
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
    
    # getter, setter
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if 1<age<120:
            self.__age=age
        else:
            print("Error AGE (1;120)")

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name
    
    #методи класу => def
    def say_something(self,words):
        print(f"Human {self.__name} say: '{words}'")
    
    def print_info(self)->None:
        print(f"Human {self.__name} has {self.__age} yeas old")
   
    # рядкове представлення обєкта Human
    def __str__(self) -> str:
        return f'Human: {self.__name}, {self.__age} year old'



class Student(Human):
    """Клас Student"""
    def __init__(self, name, age, number_gradebook, group="ЦТ-21"):
        super().__init__(name,age)
        # Human.__init__(self, name, age)
        self.__number_gradebook=number_gradebook
        self.__group=group

    def get_number_gradebook(self):
        return self.__number_gradebook
    
    def set_number_gradebook(self,number_gradebook):
        self.__number_gradebook=number_gradebook
    
    def get_group(self):
        return self.__group
    
    def set_group(self,group):
        self.__group=group

    def print_info(self)->None:
        # print(f"Human {super().get_name()} has {super().get_age()} yeas old")
        # print(f"Human {Human.get_name(self)} has {Human.get_age(self)} yeas old")
        super().print_info()
        print(f"Group: {self.__group}. GradeBook # {self.__number_gradebook}")
    
    # # # перевантаження оператора  self > other_student
    def __gt__(self, other_student):
        return self.get_age()>other_student.get_age()
    
    def __eq__(self, other_student):
        return self.get_age()==other_student.get_age() and self.get_name()==other_student.get_name()
    
    def __str__(self) -> str:
        return super().__str__()+f" (Group: {self.__group}. GradeBook #{self.__number_gradebook})"

# клас, який визначанє професію
class Employee():
    def __init__(self,profession="developer") -> None:
        self.__profession=profession

    # create getter => @property
    @property
    def profession(self):
        return self.__profession 
    
    # create setter    @[name_property_getter].setter
    @profession.setter
    def profession(self,profession):
        self.__profession=profession

    def print_info(self):
        print(self.profession)

    def __str__(self):
        return self.profession
    
class WorkingStudent(Student,Employee):
    __doc__="Info about working student (Student,Employee)"
    
    def __init__(self, name, age, number_gradebook, group, profession):
        # print(name, age, number_gradebook, group, profession)
        Student.__init__(self,name,age, number_gradebook, group)
        Employee.__init__(self,profession)

    def print_info(self):
        # super().print_info() # default call Student
        Student.print_info(self)
        Employee.print_info(self) #=>    print(Employee.__str__(self))

    def __str__(self):
        return Student.__str__(self)+" "+ Employee.__str__(self)

# ===============using class===============
# human1=Human()
# human2=Human("Olga")
# human2=Human("Olga",18)

student1=Student("Роман",19,"123/23-01","ЦТ-21")
student12=Student("Роман",20,"123/23-01","ЦТ-21")
student2=Student("Аліна",18,"123/23-02","ЦТ-21")
student3=Student("Дмитро",19,"123/23-03","ЦТ-11(3р.н.)")
print(student1.get_name())
student1.print_info()
print(student1)
print(student2)
print(student3)
print(student1>student2)
print(student1==student12)


# # використання властивостей класу Employee
developer=Employee()
ingener=Employee("ingener")
print(developer.profession)
print(ingener.profession)
developer.profession="FullStack Developer"
print(developer.profession)

wstudent=WorkingStudent("Pavlo",23,"3423/45-09","ЦТ-11","Developer Java")
wstudent.print_info()
print(wstudent)
print(WorkingStudent.mro())