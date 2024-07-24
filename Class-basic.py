class Animal:   #base class
    def walk(self):
        print('Walking.....')

class dog(Animal):  #inheritance
    def __init__(self,name,age):    #constructor
        self.name=name
        self.age=age

    def bark(sound):    #method
        print('woollff!!!!')

monir = dog('Monirujjaman',7)   #object

print(monir.age)
print(monir.name)
monir.bark()
monir.walk()