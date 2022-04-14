from random import shuffle
from Consts import Const


def generate_bricks():
    bricks = list()
    for i in range(0, 7):
        for j in range(i, 7):
            bricks.append((i, j))
    return bricks


def two_groups(bricks):
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
        return 'computer'
    elif (6, 6) in Const.PLAYER_GROUP:
        return 'player'
    elif (5, 5) in Const.COMPUTER_GROUP:
        return 'computer'
    elif (5, 5) in Const.PLAYER_GROUP:
        return 'player'
