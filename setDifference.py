e = int(input())

Eng = list(map(int, input().split()))
Eng = set(Eng)

f = int(input())

Fr = list(map(int, input().split()))
Fr = set(Fr)

diff = Eng.difference(Fr)

print(len(diff))