class Vehicle: 
    def __init__(self, name, max_speed, price=1000):
        self.name = name
        self.max_speed = max_speed
        self.price = price
        self.fare = 0

    def farex(self):
        if self.max_speed >= 80:
             self.fare = self.price * 0.1 
        else:
             self.fare = self.price * 0.05
        print(f"Fare of vehicle: {self.fare}")
        return self.fare

    def totalPrice(self):
        total = self.price + self.fare
        print(f"Total price of vehicle: {total}")

    def changespeed(self, newspeed):
        oldspeed = self.max_speed
        self.max_speed = newspeed
        print(f"Changed speed: {oldspeed} -> {self.max_speed}")
        self.farex()
        self.totalPrice()

class Bus(Vehicle): 
    def __init__(self, name, max_speed, price=1000):
        super().__init__(name, max_speed, price)

    def show(self):
        print(f"This is a bus: {self.name} with max speed = {self.max_speed}")

class XeKhach(Vehicle):
    def __init__(self, name, max_speed, price=1500):
        super().__init__(name, max_speed, price)
        self.dichden = ""
        self.khoihanh = ""

    def tuyenduong(self, dichden, khoihanh):
        self.dichden = dichden
        self.khoihanh = khoihanh
        print(f"Chuyến xe khách {self.name}: {self.khoihanh} -> {self.dichden}")

class CarInfo(XeKhach):
    def __init__(self, name, max_speed, price, dichden="Chưa rõ", khoihanh="Chưa rõ"):
        super().__init__(name, max_speed, price)
        self.dichden = dichden
        self.khoihanh = khoihanh
        self.category = "Normal"

    def classifylevel(self):
        if self.price > 1000:
            self.category = "VIP"
        else:
            self.category = "Normal"

    def infocar(self):
        print("\n" + "="*25)
        print("DETAIL REPORT VEHICLE")
        print(f"Name: {self.name}")
        print(f"Max speed: {self.max_speed}")
        self.farex()
        self.totalPrice()
        self.classifylevel()
        print(f"Category: {self.category}")
        self.tuyenduong(self.dichden, self.khoihanh)
        print("="*25)


Bus1 = Bus("Toyota", 80)
Bus1.show()
Bus1.changespeed(125)

car = CarInfo("Limousine VIP", 90, 3000, "Đà Nẵng", "Hà Nội")
car.infocar()