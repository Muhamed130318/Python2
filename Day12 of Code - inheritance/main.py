from person import Person, Student

line = input().split()

fName = line[0]
lname = line[1]
idnum = line[2]

score = list(map(int, input().split()))

student = Student(fName, lname, idnum, score)

student.printPerson()
print("Grade:", student.calculate())