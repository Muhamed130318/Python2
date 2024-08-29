n = int(input("enter number: "))

lst = []

for i in range(0, n):
    element = input().split(" ")
    lst.append(element)

lst.reverse()
#print(lst, end="")

3
for x in lst:
    print(x, end=" ")