from Builder import Builder
from Manual import Manual
class ManualBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.__manual = Manual()

    def setSeats(self, number):
        self.__manual.seats = number

    def setEngine(self, engine):
        self.__manual.engine = engine

    def setTripComputer(self):
        print("ManualTripComputer")

    def setGps(self, location : str):
        print("ManualGPS")