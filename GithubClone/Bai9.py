#Bài tập 9: Cho một danh sách, hãy đưa ra tập chỉ gồm các phần tử đơn nhất (không lặp lại của các phần tử đó)
lst = [1, 8, 2, 3, 9, 1, 8]
reducedlst=[]
for i in range(len(lst)):
    if lst[i] not in reducedlst:
        reducedlst.append(lst[i])
print(reducedlst)
