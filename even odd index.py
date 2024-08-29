n = int(input("Enter how many elements in the array: "))

lst = []    
even = []
odd = []

for i in range(0, n):
    element = str(input())
    lst.append(element)

x = 0

for n in lst:
    z = 0
    test = lst[x]
    for n in test:
        if z == 0 or z % 2 == 0:
            even.append(test[z])
        else:
            odd.append(test[z])
        z += 1
    print(''.join(even), ''.join(odd))
    even = []
    odd = []    
    x += 1


