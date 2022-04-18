from random import seed, choice

txt = input()
n = int(input())

seed(n)
print(choice(txt))
