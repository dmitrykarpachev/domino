from random import randint
N = [i for i in range(10)]
k = randint(1, len(N))
step = len(N) // k
ost = len(N) % k
m_step = step + 1

last = len(N) - ost * m_step
lst = list()
for i in range(len(N) - ost * m_step + m_step, len(N) + 1, m_step):
    lst.append(N[last:i])
    last = i
last = len(N) - ost * m_step
for i in range(len(N) - ost * m_step - step, -step, -step):
    lst.insert(0, N[i:last])
    last = i
print(lst)

'''
2) -> Находим длину меньшего подмассива(целая часть от деления длины исходного массива на k), находим остаток от деления массива на малые подмассивы - это количество больших подмассивов.
    Отсчитываем от конца массива большие подмассивы.
    остальную часть массива разбиваем на мылые подмассивы.
3) -> Малые подассивы - это целая часть от деления длины массива на k, а большие массивы  на 1 больше.
4) -> Если k больше длины N, то разбить массив на подмассивы невозможно
'''
