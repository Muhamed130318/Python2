check = input("word to check for palindrome: ")

length = len(check) - 1

rev = ''

while length >= 0:
    rev = rev + check[length]
    length -= 1

#print(rev)


if check == rev:
    print(check + " is a palindrome")
else:
    print(check + " is not a palindrome")