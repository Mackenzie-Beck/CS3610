from GUIFactory import GUIFactory
from button import Button
from checkbox import Checkbox
from WinButton import WinButton
from WinCheckbox import WinCheckbox

class WinFactory(GUIFactory):
    def createButton(self) -> Button:
        return WinButton()

    def createCheckbox(self) -> 'Checkbox':
        return WinCheckbox()
    


    