lst = [1, 5, 2, 9, 11, 20]
n = len(lst)
i = 0
while (i < n-1):
    #print("Step: ", i+1)
    j = i + 1
    while (j < n):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j]= temp
        #print("Change: ", lst)
        j = i + 1
    i = i + 1
print(lst)  