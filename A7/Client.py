from Player import Player
from Damage_upgrade_strategy import Damage_upgrade_strategy
from Speed_upgrade_strategy import Speed_upgrade_strategy
from Pierce_upgrade_strategy import Pierce_upgrade_strategy

player = Player()
player.add_upgrade(Damage_upgrade_strategy())
player.add_upgrade(Speed_upgrade_strategy())
player.add_upgrade(Pierce_upgrade_strategy())
player.shoot()

