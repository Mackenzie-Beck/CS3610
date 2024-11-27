from GUIFactory import GUIFactory
from button import Button
from checkbox import Checkbox
from MacButton import MacButton
from MacCheckBox import MacCheckbox

class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()

    def createCheckbox(self) -> 'Checkbox':
        return MacCheckbox()