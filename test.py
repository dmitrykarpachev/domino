def celsius_to_fahrenheit(lst):
    return list(map(lambda C: round((C * (9 / 5)), 1) + 32, lst))


daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

temp_above_80 = list(filter(lambda val: val > 80, celsius_to_fahrenheit(daily_temp_c)))
print(temp_above_80)
print(len(temp_above_80))
