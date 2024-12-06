from abc import ABC, abstractmethod

class Hardware(ABC):
    
    def __init__(self, t = 0, v = 0):
        self.temp = t
        self.voltage = v

    def install(self) -> str:
        print(self.__name__ + " has been installed")