a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
if (a>b):
    if (a>c):
        print("-> a is the largest number")
    else:
        print("-> c is the largest number")
else:
    if(b>c):
        print("-> b is the largest number")
    else:
        print("-> c is the largest number")