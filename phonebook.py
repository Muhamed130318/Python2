n = int(input())

phonebook = {}

for i in range(n):
    key, value = input().split()
    phonebook[key] = value

while True:
    try:
        m = input()
        if m == "":
            break
        else:
            if m in phonebook.keys():
                s = m, "=", phonebook.get(m)
                s2 = ''.join(s)
                print(s2)
            else:
                print("Not found")
    except Exception as e:
        break