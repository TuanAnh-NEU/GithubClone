lst = [1, 5, 2, 9]
n = len(lst)
for i in range (0, n):
    #print("Step: ", i+1)
    for j in range (i+1, n):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j]= temp
        #print("Change: ", lst)
print(lst)