# Input the number
A = int(input("Enter a number: "))
if A % 5 == 0 and A % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")
