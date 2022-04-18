from random import choices

population = list()
weights = list()
with open('passwords.txt', 'r') as file:
    data = ''.join(list(map(lambda l: l.rstrip(), file.readlines())))
    for let in data:
        if let not in population:
            population.append(let)
            weights.append(data.count(let))
k = max(weights) + 1
weights = list(map(lambda x: k - x, weights))

print(''.join(choices(population, weights=weights, k=10)))
