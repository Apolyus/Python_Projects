# Switch only fizz only buzz only fizzbuzz based on auto increment range is given values listed

n = input("Un numar de la 0 pana la - ")
n = int(n)
list_of_values = []
val = 0
insert_case = input("Ce doresti Fizz / Buzz / FizzBuzz :")
match insert_case:
         case "Fizz":
             for itr in range(n):
                 val = val + 1
                 if val % 3 == 0 and val % 5 != 0:
                     list_of_values.append(val)
                     print(str(val) + "- Fizz")
         case "Buzz":
             for itr in range(n):
                 val = val + 1
                 if val % 5 == 0 and val % 3 != 0:
                     list_of_values.append(val)
                     print(str(val) + "- Buzz")
         case "FizzBuzz":
             for itr in range(n):
                 val = val + 1
                 if val%3==0 and val%5==0:
                     list_of_values.append(val)
                     print(str(val) + "- FizzBuzz")
         case default:
             for itr in range(n):
                 list_of_values.append(val)
                 print(str(val))
                 val = val + 1

print("Valorile cerute pentru " +insert_case)
print(list_of_values)