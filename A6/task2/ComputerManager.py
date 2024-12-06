from Computer import Computer

class ComputerManager:

    def __init__(self, computer = None):
        if computer is None:
            computer = Computer()
        self.__computer = computer

    def beginWork(self):
        print("Turning on the computer...")

        self.__computer.powerSupply.turnOn()  # 1. Power supply: Apply power.
        self.__computer.sensor.checkVoltage(self.__computer.powerSupply)  # 2. Sensors: check voltage.
        self.__computer.sensor.checkTemp(self.__computer.powerSupply)  # 3. Sensors: check temperature in the power supply.
        self.__computer.sensor.checkTemp(self.__computer.videoCard)  # 4. Sensors: check temperature in the video card.
        self.__computer.powerSupply.supplyPower(self.__computer.videoCard)  # 5. Power supply: supply power to the video card.
        self.__computer.videoCard.startup()  # 6. Video card: launch.
        self.__computer.videoCard.checkMonitorConnection()  # 7. Video card: checking connection with the monitor.
        self.__computer.sensor.checkTemp(self.__computer.ram)  # 8. Sensors: check temperature in the RAM.
        self.__computer.powerSupply.supplyPower(self.__computer.ram)  # 9. Power supply: supply power to the RAM.
        self.__computer.ram.launchDevices()  # 10. RAM: launching devices.
        self.__computer.ram.analyzeMem()  # 11. RAM: memory analysis.
        self.__computer.videoCard.displayInfo(self.__computer.ram)  # 12. Video card: displays data about RAM.
        self.__computer.powerSupply.supplyPower(self.__computer.discReader)  # 13. Power supply: supply power to the disc reader.
        self.__computer.discReader.startup()  # 14. Optical disc reader: startup.
        self.__computer.discReader.checkForDisc()  # 15. Optical disc reader: checking for disc presence.
        self.__computer.videoCard.displayInfo(self.__computer.discReader)  # 16. Video card: display information about the disc reader.
        self.__computer.powerSupply.supplyPower(self.__computer.hdd)  # 17. Power supply: supply power to the hard drive.
        self.__computer.hdd.startup()  # 18. HDD: launch.
        self.__computer.hdd.checkBootSector()  # 19. HDD: checking the boot sector.
        self.__computer.videoCard.displayInfo(self.__computer.hdd)  # 20. Video card: output data about the hard drive.
        self.__computer.sensor.checkTemp(self.__computer)  # 21. Sensors: check the temperature of all systems.


    
    def turnOff(self):
        print("Turning off the computer...")

        self.__computer.hdd.shutDown()  # 1. HDD: stopping the device.
        self.__computer.ram.clearMem()  # 2. RAM: memory clearing.
        self.__computer.ram.analyzeMem()  # 3. Working memory: memory analysis.
        self.__computer.videoCard.displayMsg("Farewell!")  # 4. Video card: display the farewell message data on the monitor.
        self.__computer.discReader.resetPosition()  # 5. Disc reader: return to original position.
        self.__computer.powerSupply.stopSupply(self.__computer.videoCard)  # 6. Power supply: stop powering the video card.
        self.__computer.powerSupply.stopSupply(self.__computer.ram)  # 7. Power supply: stop powering the RAM.
        self.__computer.powerSupply.stopSupply(self.__computer.discReader)  # 8. Power supply: stop powering the disk reader.
        self.__computer.powerSupply.stopSupply(self.__computer.hdd)  # 9. Power supply: stop powering the hard drive.
        self.__computer.sensor.checkVoltage(self.__computer.powerSupply)  # 10. Sensors check voltage.
        self.__computer.powerSupply.turnOff()  # 11. Power supply: shutdown.