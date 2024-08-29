N = int(input())

l = []

for _ in range(N):
    commands, *args = input().split() #"commands" = takes a regular string, *args = this is used to take any parameters that are written with the command,such as "insert 2 4" args[0] = 2 and args[1] = 4. 

    if commands == "insert":
        l.insert(int(args[0]), int(args[1]))
    elif commands == "remove":
        l.remove(int(args[0]))
    elif commands == "append":
        l.append(int(args[0]))
    elif commands == "sort":
        l.sort()
    elif commands == "pop":
        l.pop()
    elif commands == "reverse":
        l.reverse()
    elif commands == "print":
        print(l)