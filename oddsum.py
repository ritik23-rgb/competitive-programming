# . Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A].
A = int(input("Enter a positive number: "))
sum = 0
for i in range(1, A + 1, 2):
    sum += i
print("The sum of all odd numbers ", sum)
