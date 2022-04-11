n = int(input())
r = 0
if n <= 15527:
  r = 0
elif 15528 <= n <= 42707:
  r = 15
elif 42708 <= n <= 132406:
  r = 25
elif n >= 132407:
  r = 28
print(f'The tax for {n} is {r}%. That is {round(n * r / 100)} dollars!')
