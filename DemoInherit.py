class Vehicle:
    def __init__(self, brand, speed):
        self.brand=brand
        self.speed=speed

    def drive():
        pass

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(  brand, speed)
        self.num_doors= num_doors   

    def drive():
        pass

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand,speed)
        self.type=type

    def drive():
        pass

