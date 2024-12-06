#Bài tập 1: Cho một danh sách các số, hãy tính tổng các phần tử trong danh sách đó.
lst = [3, 4, 5, 2, 8, 11]
n = len(lst)
Sum = 0
for i in range (0, n):
    Sum = Sum + lst[i]
print(Sum)