class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        print('The age is ' + str(self.age))
        return self.age

    def getName(self):
        print('The name is ' + str(self.name))
        return self.name

    def setAge(self, age):
        self.age = age
        return self

    def setName(self, name):
        self.name = name
        return self

    def getRef(self):
        return self


p1 = Person(age=23, name='Aman')

# print(p1.getAge())
# print(p1.getName())

print(p1.setAge(2).setName('Babu').getName())


class Student(Person):
    def __init__(self, name, age, year=2000):
        super().__init__(name, age)
        self.year = year

    def welcome(self):
        print('Welcome, ' + self.name + ' to the class of ' + str(self.year))


std1 = Student(age=14, name="preeti sikka")
std1.welcome()
