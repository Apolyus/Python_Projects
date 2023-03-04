how_many_tries = 3
try_count = 0
while try_count < how_many_tries:
    try:
        age = int(input("Put your age :"))
    except ValueError:
        print("Invalid data value")
        try_count += 1
        print(f"You have {how_many_tries-try_count} chances remaining")
        continue
    if int(age) < 18:
        print("Minor")
    else:
        print("Major")
    break
else:
    print("You have exceeded the maximum amount of tries.")
