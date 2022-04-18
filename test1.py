from random import seed, shuffle

seed(43)
txt = input().split(' ')
shuffle(txt)
print(' '.join(txt))
