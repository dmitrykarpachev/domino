from random import shuffle
from Consts import Const


def generate_bricks():
    return [(i, j) for i in range(7) for j in range(i, 7)]


def two_groups(bricks: list):
    group1 = bricks[:7]
    group2 = bricks[7:14]
    if not ((5, 5) in bricks[:14] or (6, 6) in bricks[:14]):
        shuffle(bricks)
        two_groups(bricks)
    else:
        Const.COMPUTER_GROUP, Const.PLAYER_GROUP = group1, group2
        del bricks[:14]
        Const.STOCK = bricks


def find6x6():
    if (6, 6) in Const.COMPUTER_GROUP:
        del Const.COMPUTER_GROUP[Const.COMPUTER_GROUP.index((6, 6))]
        Const.START_BRICK = (6, 6)
        return 'player'
    elif (6, 6) in Const.PLAYER_GROUP:
        del Const.PLAYER_GROUP[Const.PLAYER_GROUP.index((6, 6))]
        Const.START_BRICK = (6, 6)
        return 'computer'
    elif (5, 5) in Const.COMPUTER_GROUP:
        del Const.COMPUTER_GROUP[Const.COMPUTER_GROUP.index((5, 5))]
        Const.START_BRICK = (5, 5)
        return 'player'
    elif (5, 5) in Const.PLAYER_GROUP:
        del Const.PLAYER_GROUP[Const.PLAYER_GROUP.index((5, 5))]
        Const.START_BRICK = (5, 5)
        return 'computer'
