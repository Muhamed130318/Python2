marks = { "Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60] }

numbers = marks["Malika"]

print(numbers)

res = 0

for i in numbers:
    print(i)
    res = res + i

final = float(res/3)
print(f'{final:.2f}')
    

