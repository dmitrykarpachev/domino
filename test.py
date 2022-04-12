from random import choices

alphabet = 'qwertyuiopasdfghjklzxcvbnm'
vowels = 'aeiuojwyv'
lst = choices(alphabet, k=20)
print(list(filter(lambda x: x in vowels, lst)))