# You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A. Even numbers are those numbers that are divisible by 2.
A = int(input("Enter a positive number: "))
sum = 0
for i in range(2, A + 1, 2):
    sum += i
print("The sum of all even numbers f", sum)