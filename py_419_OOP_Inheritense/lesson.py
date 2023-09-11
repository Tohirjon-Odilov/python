class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# x = Person("John", "Doe")
# x.printname()


class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        #   Person.__init__(self, fname, lname)


x = Student("Mike", "Olsen")
x.printname()
print(x.__dict__.values())
