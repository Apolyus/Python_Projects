list_1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
#         0  1  2  3  4  5  6   7  8  9
# 1 2 3 4 5 6 7 8 9
print("list 1 : ", list_1)

print("list 2 : ", sorted(list_1))

list_3 = sorted(list_1, reverse=True)
print("list 3 : ", list_3)

list_4 = sorted(list_1)[1:9:2]

print("list pair : ", list_4)

list_5 = sorted(list_1)[0:9:2]

print("list odd : ", list_5)

list_6 = sorted(list_1)[2:9:3]

print("divisible by 3 :", list_6)
