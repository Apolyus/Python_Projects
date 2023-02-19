# enter value

val = input("Adauga un numar:")
val = int(val)
if val%3==0 and val%5==0:
     print(str(val) + "- FizzBuzz")
if val%3==0 and val%5!=0:
     print(str(val) + "- Fizz")
if val%5==0 and val%3!=0:
     print(str(val) + "- Buzz")



