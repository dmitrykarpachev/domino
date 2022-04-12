even = [0, 2, 4, 6, 8]
dod = [1, 3, 5, 7, 9]

my_sum = list(map(lambda elem: sum(elem), zip(even, dod)))
remainders = list(map(lambda a: a % 3, my_sum))
nonzero_remainders = list(filter(lambda a: a != 0, remainders))

print(remainders, nonzero_remainders)
