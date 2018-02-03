list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [7, 8, 9, 10, 11, 12, 13, 14, 15]

answer = set(list1).intersection(set(list2))
if answer:
    print("The intersections are : ", answer)
else:
    print("No intersections")
