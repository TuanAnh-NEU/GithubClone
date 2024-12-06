#Bài tập 3: Cho một danh sách và cho một giá trị nhập vào từ bàn phím, hãy cho biết phần tử đó có trong danh sách không?
#Bài tập 4: Cho một danh sách và cho một giá trị nhập vào từ bàn phím, hãy cho biết phần tử đó có trong danh sách không? trường hợp có thì cho biết vị trí đầu tiên nó xuất hiện
#Bài tập 5: Cho một danh sách và cho một giá trị nhập vào từ bàn phím,hãy cho biết phần tử đó có trong danh sách không? trường hợp có thì cho biết vị trí cuối cùng nó xuất hiện
lst = [3, 6, 9, 2, 20, 3, 3]
x = int(input("So ban muon kiem tra: "))
n = len(lst)
iexitst = False
for i in range (0, n):
    if x == lst[i]:
        iexitst = True
        a = i  # Tìm vị trí nó xuất hiện
        #break (Áp dụng cho trường hợp tìm vị trí đầu tiên nó xuất hiện hoặc muốn giảm bớt khối lượng cv)
print("         ******Ket qua******")
if iexitst == True:
    print("-> So ban da nhap co trong danh sach")
    print(" - Vi tri no xuat hien:", a)
else:
    print("-> So ban da nhap khong co trong danh sach")