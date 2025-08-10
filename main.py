from enum import Enum

class Colors(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    ORANGE = "Orange"
    PURPLE = "Purple"
    YELLOW = "Yellow"
    PINK = "Pink"
    TURQUOISE = "Turquoise"
    MAGENTA = "Magenta"
    GRAY = "Gray"
    WHITE = "White"
    BLACK = "Black"
    SILVER = "Silver"
    GOLD = "Gold"

class EngineTypes(Enum):
    class VEngines(Enum):
        V2 = "V2 (V-twin)"
        V3 = "V3"
        V4 = "V4"
        V5 = "V5"
        V6 = "V6"
        V8 = "V8"
        V10 = "V10"
        V12 = "V12"
        V14 = "V14"
        V16 = "V16"
        V18 = "V18"
        V20 = "V20"
        V24 = "V24"
        V32 = "V32"

class CarTypes(Enum):
    KFZ = "KFZ (Motor Vehicle)"
    PKW = "PKW (Car)"
    LKW = "LKW (Truck)"

class Car():
    def __init__(self, brand, ps, color, engine=EngineTypes.VEngines.V8.value, type=CarTypes.PKW.value):
        self.brand = brand
        self.ps = ps
        self.color = color
        self.engine = engine
        self.type = type
        self.position = {
            "x": 0,
            "y": 0,
            "z": 0,
        }
        self.fuel = 100

    def __str__(self):
        return f"\nBrand: {self.brand}\nPS: {self.ps}\nColor: {self.color}\nEngine-Type: {self.engine}\nCar-Type: {self.type}\nLocation:\n\tX: {self.position["x"]}\n\tY: {self.position["y"]}\n\tZ: {self.position["z"]}\nFuel: {self.fuel}%\n"
    
    def drive(self, x, y, z):
        self.position["x"] += x
        self.position["y"] += y
        self.position["z"] += z
        self.fuel -= 5

    def recolor(self, new_color):
        self.color = new_color

    def tune(self, ps):
        self.ps += ps

    def refuel(self):
        self.fuel = 100

my_car = Car("Mercedes", 500, Colors.RED.value, EngineTypes.VEngines.V8.value, CarTypes.PKW.value)
print(my_car)

my_car.drive(2, 3, 4)
my_car.recolor(Colors.BLUE.value)
my_car.tune(500)
print(my_car)

my_car.refuel()
print(my_car)