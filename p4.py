n = int(input("enter the number"))
for i in range(n,1,-1):
    for j in range(1, i + 1,):
        if j==1 or j==i:
            print("*", end="")
        else:
            print("_", end="")
    print()