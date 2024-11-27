from Director import Director
from CarBuilder import CarBuilder

director = Director()
builder = CarBuilder()
car = director.make_sports_car(builder)

print("Sports Car")
print(f"Seats: {car.seats}")
print(f"Engine: {car.engine}")
print(f"Trip Computer: {car.trip_computer}")
print(f"GPS: {car.gps}")



print("\n")
print("SUV")
car = director.make_SUV(builder)

print(f"Seats: {car.seats}")
print(f"Engine: {car.engine}")
print(f"Trip Computer: {car.trip_computer}")
print(f"GPS: {car.gps}")