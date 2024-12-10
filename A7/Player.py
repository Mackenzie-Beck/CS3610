from Bullet import Bullet

class Player:

    def __init__(self):
        self.__bullet = Bullet()
        self.__upgrades = []

    def shoot(self):
        for upgrade in self.__upgrades:
            upgrade.apply_upgrade(self.__bullet)
        print(f"Bullet shot with damage {self.__bullet.damage}, speed {self.__bullet.speed}, and pierce {self.__bullet.pierce}")

    def add_upgrade(self, upgrade):
        self.__upgrades.append(upgrade)
