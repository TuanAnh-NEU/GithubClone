#Bài tập 8: Cho một danh sách và cho một giá trị nhập vào từ bàn phím, Chừng nào còn tồn tại phần tử đó trong danh sách, hãy xóa hết nó.
lst = [3, 5, 6, 2, 9, 17]
So = input("Ban hay nhap 1 gtri bat ki: ")
n = len(lst)
for i in range (0, n):
    if lst[i] == So:
        print(i)
        list.remove(lst[i])
print(lst)