#reverse with palindrome check 

n = int(input("enter a number"))
a=n
for i in range(1, 4):
    j=n%10
    n = n // 10
    print(j, end="")
if n == a:
    print(" is a palindrome")
else:
    print(" is not a palindrome")