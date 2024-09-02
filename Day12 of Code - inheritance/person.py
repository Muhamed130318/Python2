class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName, ",", self.firstName)
        print("ID:", self.idNumber )

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        Sum = sum(self.scores)
        size = len(self.scores)
        res = Sum/size
        if res >= 90 and res <= 100:
            return "O"
        elif res >= 80 and res < 90:
            return "E"
        elif res >= 70 and res < 80:
            return"A"
        elif res >= 55 and res < 70:
            return "P"
        elif res >= 40 and res < 55:
            return "D"
        else:
            return "T"
        
