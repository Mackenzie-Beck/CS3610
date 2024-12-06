from Hardware import Hardware

class PowerSupply(Hardware):

    def turnOn(self):
        print("Turned on power supply")

    def supplyPower(self, part : Hardware):
        print(part.__name__ + " has been supplied with power")

    def stopSupply(self, part : Hardware):
        print(part.__name__ + " is no longer being supplied with power")

    def turnOff(self):
        print("Turned off power supply")
