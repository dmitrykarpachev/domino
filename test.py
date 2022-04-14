try:
  name, lastname = input().split(' ')
  print(f'Welcome to our party, {name} {lastname}')
except BaseException:
  print('You need to enter exactly 2 words. Try again!')
