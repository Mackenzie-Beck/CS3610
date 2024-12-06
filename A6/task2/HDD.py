from Hardware import Hardware

class HDD(Hardware):
    
    def startup(self):
        print("HDD has been started up")

    def checkBootSector(self):
        print("Boot sector status : Good")

    def shutDown(self):
        print("HDD has been shut off")