class Fraction:
    def __init__(self, numerator, nominator):
        self.numerator = numerator
        self.nominator = nominator

    def __str__(self):
        return f"{self.numerator}/{self.nominator}"

    def __add__(self, other1, other2):
        numerator = (self.numerator * other2) + (other1 * self.nominator)
        nominator = self.nominator * other2
        return Fraction(numerator, nominator)

    def __sub__(self, other1, other2):
        numerator = (self.numerator * other2) - (other1 * self.nominator)
        nominator = self.nominator * other2
        return Fraction(numerator, nominator)

    def __invert__(self):
        return Fraction(self.nominator, self.numerator)


if __name__ == '__main__':
    Fraction = Fraction(3, 2)
    print("The numbers are :", Fraction.__str__())
    print("Type : ", type(Fraction.__str__()))
    print("Addition : ", Fraction.__add__(2, 2))
    print("Type : ", type(Fraction.__add__(2, 2)))
    print("Subtraction : ", Fraction.__sub__(2, 2))
    print("Type : ", type(Fraction.__sub__(2, 2)))
    print("The inverted fraction is :", Fraction.__invert__())
    print("Type : ", type(Fraction.__invert__()))

