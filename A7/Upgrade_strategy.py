
from abc import ABC, abstractmethod

class Upgrade_strategy(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def apply_upgrade(self):
        pass