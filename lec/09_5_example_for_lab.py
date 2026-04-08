import random
import time
class Student:
    """
    Клас, що описує сутність студента
    """
    count_student=0 #зміна класу
    def __init__(self,name="NoName",group="Інф_ЦТ"):
        self.name = name
        self.group=group
        self.gladness = 50
        self.progress = 0
        self.alive = True
        Student.count_student=Student.count_student+1

    def __str__(self):
        return f"Student {self.name} study in group {self.group}."

    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 10

    def to_eat(self):
        print("I am eating")
        self.gladness += 10
    

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress <= -5:
            print("Passed externally...")
            self.alive = False



    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

if __name__=="__main__":
    tymofiy = Student("Tymofiy")
    print(tymofiy)
    print(Student.count_student)
    katerina = Student("Katerina","ІCT-31")
    print(katerina)
    print(Student.count_student)
    tymofiy.to_study()
    katerina.to_study()
    katerina.to_sleep()
    katerina.to_study()
    print(tymofiy)
    tymofiy.end_of_day()
    print(katerina)
    katerina.end_of_day()
    for day in range(304):
        if katerina.alive == False:
            break
        time.sleep(1)
        katerina.live(day)