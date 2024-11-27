from CarBuilder import CarBuilder
from Car import Car

class Director:
    
    def make_SUV(self, builder : CarBuilder) -> Car:
        builder.setSeats(4)
        builder.setEngine("V8")
        builder.setTripComputer()
        builder.setGps()
        return builder.getResult()

    def make_sports_car(self, builder : CarBuilder) -> Car:
        builder.setSeats(2)
        builder.setEngine("V12")
        builder.setTripComputer()
        builder.setGps()
        return builder.getResult()