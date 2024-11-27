from CarBuilder import CarBuilder
from Car import Car

class Director:
    
    def make_SUV(self) -> Car:
        builder = CarBuilder()
        builder.setSeats(4)
        builder.setEngine("V8")
        builder.setTripComputer()
        builder.setGps()
        return builder.getCar()

    def make_sports_car(self) -> Car:
        builder = CarBuilder()
        builder.setSeats(2)
        builder.setEngine("V12")
        builder.setTripComputer()
        builder.setGps()
        return builder.getCar()