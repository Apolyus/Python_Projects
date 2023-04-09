class Fractions:
    def __init__(self, numerator, nominator):
        self.numerator = numerator
        self.nominator = nominator

    def __str__(self):
        return self.numerator, self.nominator

    def __add__(self, other1, other2):
        numerator = (self.numerator * other2) + (other1 * self.nominator)
        nominator = self.nominator * other2
        return f"{numerator}/{nominator}"

    def __sub__(self, other1, other2):
        numerator = (self.numerator * other2) - (other1 * self.nominator)
        nominator = self.nominator * other2
        return f"{numerator}/{nominator}"

    def __invert__(self):

        return f"{self.nominator}/{self.numerator}"


if __name__ == '__main__':
    fractions = Fractions(3, 2)
    print("The numbers are :", fractions.__str__())
    print("Addition : ", fractions.__add__(2, 2))
    print("Subtraction : ", fractions.__sub__(2, 2))
    print("The inverted fraction is :", fractions.__invert__())

