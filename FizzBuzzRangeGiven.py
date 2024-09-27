# Auto increment range is given

n = input("Un numar de la 0 pana la - ")
n = int(n)
val = 0
for _ in range(n):
    val = val + 1
    if val%3!=0 and val%5!=0:
        print(str(val))
    if val%3==0 and val%5==0:
        print(str(val) + "- FizzBuzz")
    if val%3==0 and val%5!=0:
      print(str(val) + "- Fizz")
    if val%5==0 and val%3!=0:
      print(str(val) + "- Buzz")