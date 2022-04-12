string1 = input()
string2 = input()
print(''.join([s1 + s2 for s1, s2 in zip(string1, string2)]))