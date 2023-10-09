class Car:
    def __init__(self, make, consumption=0, km=0, price=0, gas=0):
        self.make = make
        self.consumption = consumption
        self.km = km
        self.price = price
        self.gas = gas

    def showMake(self):
        return f"Your car is a/n: {self.make}"

    def showConsumption(self):
        return f"Consumption is: {self.consumption}"

    def showKm(self):
        return f"Km: {self.km}"

    def showPrice(self):
        return f"Price: {self.price}"

    def addKm(self, addKm):
        if self.km + addKm > self.km:
            self.km += addKm
        else:
            print("Ai mers cu spatele?")

    def showGas(self):
        return f"Liters: {self.gas}"

    def addGas(self, fuel):
        if fuel > 0:
            self.gas += fuel
        else:
            print("Nu ai alimentat")


car1 = Car("BMW", 5, 68355, 38500)
print(car1.showMake())

print(car1.showConsumption())

print(car1.showKm())

print(car1.showPrice())


car1.addKm(20000)
print(car1.showKm())

print(car1.showGas())

car1.addGas(0)
print(car1.showGas())
car1.addGas(20)
print(car1.showGas())
