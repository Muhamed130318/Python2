s = "This is a string."

def cap(s):
    return ' '.join(i.capitalize() for i in s.split(" "))
    

print(cap(s))