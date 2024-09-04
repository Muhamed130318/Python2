e = int(input())

Eng = list(map(int, input().split()))
Eng = set(Eng)

f = int(input())

Fr = list(map(int, input().split()))
Fr = set(Fr)

uni = Eng.union(Fr)

print(len(uni))