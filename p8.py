n = int(input("Enter the number : "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for k in range(2 * (n - i)):
        print(" ", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()