from Hardware import Hardware

class OpticalDiscReader(Hardware):
    def startup(self):
        print("Optical disc reader started")

    def checkForDisc(self):
        print("Presence of disc confirmed")

    def resetPosition(self):
        print("Position of disc reader has been reset")