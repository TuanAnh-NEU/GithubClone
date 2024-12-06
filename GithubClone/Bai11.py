#Bài tập 11: Cho một danh sách các số, hãy sắp xếp các phần tử trong danh sách tăng dần
lst = [1, 3, 5, 6, 3, 9, 33, 22]
print(lst)
for i in range (0, len(lst) -1):
    for j in range (i, len(lst)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
            