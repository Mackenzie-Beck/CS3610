from Hardware import Hardware

class VideoCard(Hardware):
    
    def startup(self):
        print("Video card has been started up")
    
    def checkMonitorConnection(self):
        print("Monitor connection checked")
    
    def displayInfo(self, part : Hardware):
        print(type(part).__name__ + " status: Good")
    
    def displayMsg(self, msg : str):
        print(msg)
