from Sensor import Sensor
from OpticalDiscReader import OpticalDiscReader
from PowerSupply import PowerSupply
from RAM import RAM
from VideoCard import VideoCard
from HDD import HDD

class Computer():

    def __init__(self, videoCard = None, ram = None, hdd = None, discReader = None, powerSupply = None, sensor = None):
        if videoCard is None:
            videoCard = VideoCard()  # Create a default VideoCard instance
        if ram is None:
            ram = RAM()  # Create a default RAM instance
        if hdd is None:
            hdd = HDD()  # Create a default HDD instance
        if discReader is None:
            discReader = OpticalDiscReader()  # Create a default DiscReader instance
        if powerSupply is None:
            powerSupply = PowerSupply()  # Create a default PowerSupply instance
        if sensor is None:
            sensor = Sensor()  # Create a default Sensor instance

        self.videoCard = videoCard
        self.ram = ram
        self.hdd = hdd
        self.discReader = discReader
        self.powerSupply = powerSupply
        self.sensor = sensor

        