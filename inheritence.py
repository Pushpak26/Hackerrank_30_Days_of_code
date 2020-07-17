class Person:
    def __init__(self, firstname, lastname, idnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.idnumber = idnumber

    def printPerson(self):
        print("Name:", self.lastname + ",", self.firstname)
        print("ID:", self.idnumber)

class Student(Person):
    def __init__(self, firstname, lastname, idnumber, testscores):
        super().__init__(firstname, lastname, idnumber)
        self.testscores = testscores

    def calculate(self):
        total = 0

        for testscore in self.testscores:
            total += testscore
        avg = total / len(self.testscores)

        if 90 <= avg <= 100:
            return "O"
        if 80 <= avg <= 90:
            return "E"
        if 70 <= avg <= 80:
            return "A"
        if 55 <= avg <= 70:
            return "P"
        if 40 <= avg <= 55:
            return "D"
        return "T"

line = input().split()
firstname = line[0]
lastname = line[1]
idnumber = line[2]
numscores = int(input())
scores = list(map(int, input().split()))
s = Student(firstname, lastname, idnumber, scores)
s.printPerson()
print("Grade", s.calculate())