
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return 'This person is called {n} and is {a} years old'.format(n = self.name, a = self.age)



me = Person('Jon', 2321)

print(me.show())


