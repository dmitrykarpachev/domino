from random import randint
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
revenues = [randint(1000, 10000) for _ in range(12)]
costs = [randint(0, v - 500) for v in revenues]
profits = [r - c for r, c in zip(revenues, costs)]

for j, (m, p) in enumerate(list(zip(month, profits))[1:]):
    pers = round((p - profits[j - 1]) / (profits[j - 1] / 100))
    s = str()
    if pers >= 50:
        s = 'great'
    elif 50 > pers >= 25:
        s = 'decent'
    elif 25 > pers >= 0:
        s = 'need follow up'
    elif pers < 0:
        s = 'critical'
    print(m, p, pers, s)
