# print(complex(2,3))
# # drib(2,3)  => 2/3

# a=complex(3,4)
# b=complex(-2,3)
# print(a+b)

class Drib():
    def __init__(self,numerator,denominator) -> None:
        self.numerator=numerator
        self.denominator=denominator
    
    def __repr__(self):
        return "Drib("+str(self.numerator)+","+str(self.denominator)+")"

    def __str__(self) -> str:
        if self.numerator>self.denominator:
           return f"{self.numerator//self.denominator} {self.numerator%self.denominator}/{self.denominator}"
        return f"{self.numerator}/{self.denominator}"
    
    # +
    def __add__(self,other):
        c=Drib(1,1)
        if isinstance(other, Drib):
            c.numerator=self.numerator*other.denominator+self.denominator*other.numerator
            c.denominator=self.denominator*other.denominator
        elif  isinstance(other, int):
            c.numerator=self.denominator*other+self.numerator
            c.denominator=self.denominator
        return c
    
    # +
    def __radd__(self,other):
        c=Drib(1,1)
        if isinstance(other, Drib):
            c.numerator=self.numerator*other.denominator+self.denominator*other.numerator
            c.denominator=self.denominator*other.denominator
        elif  isinstance(other, int):
            c.numerator=self.denominator*other+self.numerator
            c.denominator=self.denominator
        return c
    # ==
    def __eq__(self, other) -> bool:
        if self.numerator*other.denominator==other.numerator*self.denominator:
            return True
        return False
    



a=Drib(2,3) # 2/3
b=Drib(2,5) # 2/5
print(a)
print(b)
print(a+b)
c=a+b
print(c)
print(f"{a}=={b} => {a==b}")
print(f"{Drib(1,2)}=={Drib(1,2)} => {Drib(1,2)==Drib(1,2)}")
print(f"{a}+3={a+3}")
print(f"3+{a}={3+a}")

# d=Drib(a) #TypeError: Drib.__init__() missing 1 required positional argument: 'denominator
# d=repr(a)
# print(d)
