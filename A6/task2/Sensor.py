from Hardware import Hardware

class Sensor(Hardware):

    def checkVoltage(self, part : Hardware):
        print("Voltage of " + part.__name__ + " checked")
    
    def checkTemp(self, part : Hardware):
        print("Temperature of " + part.__name__ + " checked")