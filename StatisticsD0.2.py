n = int(input())
if n >= 5 and n <= 50:
    numbers = list(map(int, input().split()))
    weight = list(map(int, input().split()))

    res = []

    for i in range(0, len(numbers)):
        res.append(numbers[i] * weight[i])

    numberWeightSum = sum(res)
    weightSum = sum(weight)

    weightedMean = numberWeightSum/weightSum

    print(round(weightedMean, 1))