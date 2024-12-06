from Bullet import Bullet

class Player:

    def __init__(self):
        self.bullet = Bullet()
        self.upgrades = []

    def shoot(self):
        for upgrade in self.upgrades:
            upgrade.apply_upgrade(self.bullet)
        print(f"Bullet shot with damage {self.bullet.damage}, speed {self.bullet.speed}, and pierce {self.bullet.pierce}")

    def add_upgrade(self, upgrade):
        self.upgrades.append(upgrade)
