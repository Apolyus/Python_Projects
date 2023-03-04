# FizzBuzz Bop It

import sys

print ("Alege gradul de dificultate ")
n = input("Un numar de la 0 pana la - ")
n = int(n)
list_of_values = []
val = 0
print ("Introduceti valorile corecte")
for itr in range(n):
    val = val + 1
    if val % 3 == 0 and val % 5 != 0:
        insert_case = input(str(val) + " : Ce este Fizz / Buzz / FizzBuzz :")
        match insert_case:
            case "Fizz":
                print(str(val) +" "+ insert_case +" "+ "Corect")
            case default :
              print(str(val) +" "+ insert_case +" "+ "Gresit")
              sys.exit(1)

    if val % 5 == 0 and val % 3 != 0:
        insert_case = input(str(val) + " : Ce este Fizz / Buzz / FizzBuzz :")
        match insert_case:
            case "Buzz":
                print(str(val) +" "+ insert_case +" "+ "Corect")
            case default :
              print(str(val) +" "+ insert_case +" "+ "Gresit")
              sys.exit(1)

    if val % 3 == 0 and val % 5 == 0:
        insert_case = input(str(val) + " : Ce este Fizz / Buzz / FizzBuzz :")
        match insert_case:
            case "FizzBuzz":
                print(str(val) +" "+ insert_case +" "+ "Corect")
            case default :
              print(str(val) +" "+ insert_case +" "+"Gresit" )
              sys.exit(1)

