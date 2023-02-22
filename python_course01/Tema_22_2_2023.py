<<<<<<< HEAD
list_1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
#         0  1  2  3  4  5  6   7  8  9
print("list 1 : ", list_1)

print("list 2 : ", sorted(list_1))

list_3 = sorted(list_1, reverse=True)

print("list 3 : ", list_3)

list_4 = list_1[1:4:2]

list_5 = list_1[6:8:1]

list_6 = list_1[-1:]

print("list pair : ", list_4+list_5+list_6)

list_7 = list_1[0:4:2] + list_1[5:9:3]

print("list odd : ", list_7)

list_for_intersect = [3, 6, 9]
list_8 = set(list_1).intersection(list_for_intersect)

print("intersection :", sorted(list_8))
=======
list_1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
#         0  1  2  3  4  5  6   7  8  9
print("list 1 : ", list_1)

print("list 2 : ", sorted(list_1))

list_3 = sorted(list_1, reverse=True)

print("list 3 : ", list_3)

list_4 = list_1[1:4:2]

list_5 = list_1[6:8:1]

list_6 = list_1[-1:]

print("list pair : ", list_4+list_5+list_6)

list_7 = list_1[0:4:2] + list_1[5:9:3]

print("list odd : ", list_7)

list_for_intersect = [3, 6, 9]
list_8 = set(list_1).intersection(list_for_intersect)

print("intersection :", sorted(list_8))
>>>>>>> origin/main
