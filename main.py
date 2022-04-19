from Funcs import *
from Consts import Const
from COMPUTER import Computer
from PLAYER import Player
from PLANE import Plane
from Exceptions import *

try:
    level = int(input('You take the difficulty level(0, 1, 2): '))
except BaseException:
    level = 0
print('=' * 70)
two_groups(generate_bricks())
s = find6x6()
computer = Computer(Const.COMPUTER_GROUP, level)
player = Player(Const.PLAYER_GROUP, level)
plane = Plane(player, computer, Const.STOCK, s, Const.START_BRICK)

game = True
while game:
    f = plane.finish()
    if f is not None:
        print('※' * 70)
        print(f)
        print('※' * 70)
        break
    print('Stock size:', len(plane))
    print('Computer pieces:', len(computer))
    print(f'Player pieces: {len(player)}\n' + str(player))
    print('-' * 70)
    print(plane)
    run = True
    while run:
        command = input()
        try:
            plane.step(command)
        except InvalidInput:
            print('You have entered an invalid value. Try again!')
        except InvalidIndex:
            print('You do not have a dice with this number!')
        except ConnectError:
            print('Bone cannot be connected! Make the right choice.')
        else:
            run = False
