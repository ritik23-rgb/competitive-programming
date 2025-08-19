#. Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N.

N = int(input("Enter a number: "))
sum = 0
while N > 0:
    digit = N % 10
    sum += digit
    N //= 10
print("sum", sum)