def decimalToBinary(n): 
    return bin(n).replace("0b", "") 

n = int(input("Enter number to convert to binary: "))

if n > 1 and n < 1000000:
    s2 = decimalToBinary(n)

    lst = []

    for i in s2:
        lst.append(i)

    for i in range(0, len(lst)):
        lst[i] = int(lst[i])

    tempOne = 0
    one = 0
    for i in range(0, len(lst)):
        if lst[i] == 1:
            tempOne += 1
            if tempOne > one:
                one = tempOne
        else:
            tempOne = 0
    print("The largest amount of consecutive ones in the binary form of", n, "is", one)
    