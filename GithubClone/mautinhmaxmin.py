lst = [15, 10, 3, 8, 2, 4, 14, 6, 15, 15, 6, 8, 3, 3, 9, 15, 7]
#Cho dãy số 
maxvalue = lst[0]
n=len(lst)
#Cho biến maxvalue gán vs gtri đầu tiên của dãy số
for x in lst:
    if maxvalue < x:
        maxvalue = x
        #Gán giá trị lớn nhất tạm thời bằng x
print("Maxvalue:",maxvalue)
for i in range (0, n):
    if maxvalue == lst[i]:
        print("Vtri:",i)
    

#Trong đoạn code trên gia sử đặt max là phần tử cuối cùng hay đầu tiên cũng được. Nếu không đặt mà bạn gán max ban đầu là 0 nhưng nếu TH list trên là số nhỏ hơn 0 thì max là 0 nên sẽ bị sai 