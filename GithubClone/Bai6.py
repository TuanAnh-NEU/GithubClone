#Bài tập 6: Cho một danh sách và cho một giá trị nhập vào từ bàn phím, hãy cho biết phần tử đó xuất hiện bao nhiêu lần trong danh sách đó
mystr = input("Nhập dãy số bạn muốn tính: ")
x = input("Bạn hãy nhập số bạn muốn kiếm số lần lặp: ")
lst = mystr.split()
print(lst)
n = len(lst)
Solanlap = 0
for i in range (0, n):
    if lst[i] == x:
        Solanlap = Solanlap + 1
        print(" Vtri của số đó trong ds: ", i)
print("Số lần lặp là: ", Solanlap)