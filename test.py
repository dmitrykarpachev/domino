from random import randint

names = ['Денис', 'Дима', 'Ваня', 'Дима', 'Дима', 'Лёха', 'Вова', 'Вадим', 'Богдан', 'Юра', 'Антон', 'Артем', 'Костя']
maths = [randint(25, 50) for _ in range(13)]
physics = [randint(25, 50) for _ in range(13)]
english = [randint(25, 50) for _ in range(13)]

print([name for name, m, p, e in zip(names, maths, physics, english) if m + p + e >= 100])
