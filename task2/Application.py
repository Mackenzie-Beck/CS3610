from GUIFactory import GUIFactory
import platform
from MacFactory import MacFactory
from WinFactory import WinFactory

class Application: 
    def __init__(self) -> None:
        self.factory = None
        self.button = None
        self.checkOS()




    def checkOS(self) -> None:
        if platform.system() == "Darwin":
            self.factory = MacFactory()
        elif platform.system() == "Windows":
            self.factory = WinFactory()
        else:
            raise ValueError("Unsupported OS")

    def createUI(self) -> None: 
        self.button = self.factory.createButton()
        self.checkbox = self.factory.createCheckbox()

    def paint(self) -> None: 
        self.button.paint()
        self.checkbox.paint()