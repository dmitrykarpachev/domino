from Funcs import *
from Consts import Const
from COMPUTER import Computer
from PLAYER import Player
from PLANE import Plane

two_groups(generate_bricks())
computer = Computer(Const.COMPUTER_GROUP)
player = Player(Const.PLAYER_GROUP)
plane = Plane(Const.STOCK)
