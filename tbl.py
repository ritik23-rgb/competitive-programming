#Take a number A as input, print its multiplication table having the first 10 multiples
A = int(input("Enter a number: "))
for i in range(1, 11):
    print(A, "x", i, "=", A * i)
    