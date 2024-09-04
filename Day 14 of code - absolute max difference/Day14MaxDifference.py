class Difference:
    def __init__(self, lst):
        self.__elements = lst
        self.maxDifference = 0
    def computeDifference(self):
        i = 0
        n = i+1
        temp = 0
        for i in self.__elements:
            for n in self.__elements:
                temp = abs(i - n)
                if temp > self.maxDifference:
                    self.maxDifference = temp
        return self.maxDifference

n = int(input())
lst1 = list(map(int, input().split()))


lst = Difference(lst1)

lst.computeDifference()

print(lst.maxDifference)