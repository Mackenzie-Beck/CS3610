from Upgrade_strategy import Upgrade_strategy

class Pierce_upgrade_strategy(Upgrade_strategy):
    def __init__(self):
        self.pierce_increase = 1

    def apply_upgrade(self, bullet):
        bullet.pierce += self.pierce_increase
        print(f"Bullet pierce increased to {bullet.pierce}")