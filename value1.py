# user input for n and prnt all the values till n .




n = int(input("enter a value for n: "))
for i in range(1,n+1):
    if i % 2 != 0:
        print(i, end=' ')