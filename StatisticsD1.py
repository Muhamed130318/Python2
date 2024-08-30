n = int(input())
lst = list(map(int, input().split()))
lst.sort()

def evenCalc(list):
    leftMid = list[(len(list)//2)-1]
    rightMid = list[len(list)//2]
    median = (leftMid + rightMid)//2
    return(median)

def oddCalc(list):
    n = []
    for i in range(len(list)//2, len(list)):
        n.append(list[i])
    median = n.pop(0)
    return(median)

def halfMedian(list):
    lHalf = []
    rHalf = []
    if len(list) % 2 == 0:
        for i in range(0, len(list)//2):
            lHalf.append(list[i])
        for i in range(len(list)//2, len(list)):
            rHalf.append(list[i])
    else:
        for i in range(0, len(list)//2):
            lHalf.append(list[i])
        for i in range(len(list)//2, len(list)):
            rHalf.append(list[i])
        rHalf.pop(0)

    if len(lHalf) % 2 == 0 and len(rHalf) % 2 == 0:
        return evenCalc(lHalf), evenCalc(rHalf)
    else:
        return oddCalc(lHalf), oddCalc(rHalf)

s = halfMedian(lst)
res = [*s]

if len(lst) % 2 == 0:
    n = evenCalc(lst)
else:
    n = oddCalc(lst)

res.insert(1, n)
for i in res:
    print(i)