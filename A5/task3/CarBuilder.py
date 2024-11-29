from Builder import Builder
from Car import Car

class CarBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.__car = Car()

    def setSeats(self, number):
        self.__car.seats = number

    def setEngine(self, engine):
        self.__car.engine = engine

    def setTripComputer(self):
        self.__car.trip_computer = 0

    def setGps(self):
        self.__car.gps = None


    def getResult(self) -> Car:
        return self.__car