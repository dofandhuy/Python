class Animal():
    def identify(self):
        print("This is an animal")
        return;
class Dog(Animal):
    def Bark(self):
        print("Gou Gou")

class Cat(Animal): 
    def Bark(self):
        print("Meow Meow")

class Cow(Animal):
    def Speak(self):
        print("Mo Mo")

d= Animal()
d.identify()
e= Cow()
e.identify()
e.Speak()
c= Cat()
c.Bark()
c.identify()
a=Dog()
a.identify()
a.Bark()
