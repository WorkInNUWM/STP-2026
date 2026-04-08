from abc import ABCMeta, abstractmethod
class Pet(metaclass = ABCMeta):
    def __init__(self, name, type):
        """ Конструктор
        :param name: Кличка тварини
        """
        self.__name = name # приватне поле - кличка тварини
        self.__type=type
    
    @abstractmethod
    def voice(self): # абстрактний метод
        pass # порожня реалізація

    @abstractmethod
    def eat(self):
        print(f"Pet eat, as {self.__type}  {self.__name}:")


class Cat(Pet):
    def __init__(self, name):
        """ Конструктор
        :param name: Кличка тварини
        """
        super().__init__(name, type="cat")
        self.__name = name # приватне поле - кличка тварини
    
    def voice(self): # 
        print("may")
   
    def eat(self):
        super().eat()
        print("milk, meat")
    
    def __voice(self): # 
        print("may")
      
class Dog(Pet):
    def __init__(self, name):
        """ Конструктор
        :param name: Кличка тварини
        """
        super().__init__(name, type="dog")
        self.__name = name # приватне поле - кличка тварини
    
    def voice(self): # 
        print("Gav-gav")
   
    def eat(self):
        super().eat()
        print("meat amd meat")

    def __voice(self): # 
        print("may")
   
# pet= Pet("Rokky")
cat=Cat("Tom")
cat.eat()
cat.voice()
dog=Dog("Chapa")
dog.eat()

pets=[cat, dog, Cat("Pushok"),Dog("rex")]
print("Info our pets:")
count=1
for pet in pets:
    print(f"{count}. ",end="")
    pet.eat()
    count+=1