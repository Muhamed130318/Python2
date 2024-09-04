n = int(input())
s = set()

def avg(list):
    return (sum(set(list))/len(set(list)))


for i in range(n):
    element = input()
    s.add(element)

print(len(s))