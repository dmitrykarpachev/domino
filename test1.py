from random import randint


while True:
    a, b = randint(1, 6), randint(1, 6)
    if a == b and a in (5, 6):
        print(a, b)
        break
