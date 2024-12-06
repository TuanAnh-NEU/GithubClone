lst = [3, 5, 7, 4, 12, 9, 15]
Tong = 0
sochuso = 0
max = lst[0]
min = lst[0]
n = len(lst)
for i in range (0, n):
    Tong = Tong + lst[i]
    if max < lst[i]:
        max = lst[i]
    if min > lst[i]:
        min = lst[i]
print("Ket qua tim duoc la:")
print("- Max:", max)
print("- Min:", min)
print("- Average: ", Tong/n)