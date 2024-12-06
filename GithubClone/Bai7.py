#Bài tập 7: Cho một danh sách và cho một giá trị nhập vào từ bàn phím, Nếu có phần tử đó trong danh sách, hãy xóa phần tử tại vị trí đầu tiên nó xuất hiện
lst = [3, 5, 6, 2, 9, 17]
x = int(input("Ban hay nhap 1 gtri bat ki: "))
print("Danh sach ban dau", lst)
while x in lst:
    lst.remove(x)
print("Sau khi cat bot", lst)