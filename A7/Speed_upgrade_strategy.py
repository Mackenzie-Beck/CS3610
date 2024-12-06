from Upgrade_strategy import Upgrade_strategy

class Speed_upgrade_strategy(Upgrade_strategy):
    def __init__(self):
        self.speed_increase = 1 

    def apply_upgrade(self, bullet):
        bullet.speed += self.speed_increase
        print(f"Bullet speed increased to {bullet.speed}")