from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setSeats(self, number):
        pass

    @abstractmethod
    def setEngine(self, engine):
        pass

    @abstractmethod
    def setTripComputer(self):
        pass

    @abstractmethod
    def setGps(self):
        pass
