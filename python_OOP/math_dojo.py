
class MathDojo:
    def __init__(self, number):
        self.number = number

    def add(self, *args):
        for value in args:
            self.number += value
        return self

    def subtract(self, *args):
        for value in args:
            self.number -= value
        return self

    def result(self):
        print(self.number)
        return self

md=MathDojo(0)
print(md.number)
md.add(2).add(2,5,1).subtract(3,2).result()

