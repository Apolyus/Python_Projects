class Fractions:
    def __init__(self, numerator, nominator):
        self.numerator = numerator
        self.nominator = nominator

    def __str__(self):
        return self.numerator, self.nominator

    def __add__(self, other1, other2):
        final = self.numerator / self.nominator + other1/other2
        return final

    def __sub__(self, other1, other2):
        final = self.numerator / self.nominator - other1/other2
        return final

    def __invert__(self):
        division = self.numerator / self.nominator
        final = 1/division
        return final


if __name__ == '__main__':

    fractions = Fractions(3, 2)
    print("The numbers are :", fractions.__str__())
    print("The fraction + 1 is : ", fractions.__add__(2, 2))
    print("The fraction - 1 is : ", fractions.__sub__(2, 2))
    print("The inverted fraction is :", fractions.__invert__())

