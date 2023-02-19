# auto incremente range 200
val = 0
for _ in range(200):
        val = val + 1
        if val%3!=0 and val%5!=0:
            print(str(val))
        if val%3==0 and val%5==0:
            print(str(val) + "- FizzBuzz")
        if val%3==0 and val%5!=0:
            print(str(val) + "- Fizz")
        if val%5==0 and val%3!=0:
            print(str(val) + "- Buzz")