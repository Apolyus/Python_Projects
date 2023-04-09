class Fractions:
    def __init__(self, numerator, nominator):
        self.numerator = numerator
        self.nominator = nominator

    def __str__(self):
        return f"{self.numerator} {self.nominator}"

    def __add__(self, other):
        division = self.numerator / self.nominator
        final = division + other
        return f"{final}"

    def __sub__(self, other):
        division = self.numerator / self.nominator
        final = division - other
        return f"{final}"

    def __invert__(self):
        division = self.numerator / self.nominator
        final = 1/division
        return f"{final}"


if __name__ == '__main__':

    fractions = Fractions(4, 2)
    print("The numbers are :", fractions.__str__())
    print("The fraction + 1 is : ", fractions.__add__(1))
    print("The fraction - 1 is : ", fractions.__sub__(1))
    print("The inverted fraction is :", fractions.__invert__())