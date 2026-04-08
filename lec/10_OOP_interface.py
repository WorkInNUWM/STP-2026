from abc import ABCMeta, abstractmethod
class Diagnosable(metaclass=ABCMeta):
    @abstractmethod
    def diagnose(self):
        """ Абстрактний метод діагностувати """
        pass
    

class Car:
    def __init__(self, resource=100000):
        """ Конструктор
        :param resource: ресурс автомобіля до капітального ремонту
        """
        self._resource = resource
        self._current_mileage = 0 # поточний пробіг автомобіля
    
    def driving(self):
        self._current_mileage += 15000


class Human:
    def __init__(self):
        """ Конструктор """
        self._health = 100 # Рівень здоров'я у відсотках
    
    def eat(self, food):
        if food == "junk food": # шкідливий продукт
            self._health -= 20 # погіршує здоров'я
        elif food == "healthy food": # корисний продукт
            self._health += 20 # покращує здоров'я
        self._health = self._health if self._health > 0 else 0
        self._health = self._health if self._health < 100 else 100
        
 
class DiagnosableCar(Car, Diagnosable):
    def diagnose(self):
        if self._current_mileage >= self._resource:
           return "Your car requires major repairs!"
        rest = self._resource - self._current_mileage
        rest /= self._resource
        rest *= 100
        return "Rest {}% of resource".format(rest)


class DiagnosableHuman(Human, Diagnosable):
    def diagnose(self):
        if self._health <= 0:
           return "A junk food has killed you!"
        elif self._health == 100:
            return "You have a great health!"
        else:
            return "Please, visit a doctor "


c = DiagnosableCar()
h = DiagnosableHuman()
for i in range(5):
    c.driving()
    h.eat("junk food")

print(c.diagnose())
print(h.diagnose())