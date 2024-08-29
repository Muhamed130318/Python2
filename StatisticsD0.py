n = int(input())

lst = list(map(int, input().split()))

def mean(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    
    res = sum/len(numbers)
    print(res)

def median(numbers):
    length = len(numbers)
    numbers.sort()
    if length % 2 == 0:
        right = numbers[length // 2 - 1]
        left = numbers[length // 2]
        sum = right + left
        result = sum / 2
    else:
        result = numbers[length // 2]
    print(result)

def mode(numbers):
    counter = 0
    num = numbers[0]

    for i in numbers:
        freq = numbers.count(i)
        if freq > counter:
            counter = freq
            num = i

    if counter <= 1:
        numbers.sort()
        num = numbers[0]

    print(num)

mean(lst)
median(lst)
mode(lst)
