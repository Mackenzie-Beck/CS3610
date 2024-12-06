from Upgrade_strategy import Upgrade_strategy

class Damage_upgrade_strategy(Upgrade_strategy):
    def __init__(self):
        self.damage_increase = 1

    def apply_upgrade(self, bullet):
        bullet.damage += self.damage_increase
        print(f"Bullet damage increased to {bullet.damage}")