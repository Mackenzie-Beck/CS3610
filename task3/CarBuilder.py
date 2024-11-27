from Builder import Builder

class CarBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def setSeats(self, number):
        self.car.seats = number

    def setEngine(self, engine):
        self.car.engine = engine

    def setTripComputer(self):
        self.car.trip_computer = 0

    def setGps(self, location : str):
        self.car.gps = location
