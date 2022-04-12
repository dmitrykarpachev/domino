vec1 = tuple(map(int, input().split(' ')))
vec2 = tuple(map(int, input().split(' ')))

print(f'v1 = {vec1} & v2 = {vec2}')
for v1, v2 in zip(vec1, vec2):
    print(v1 + v2)
