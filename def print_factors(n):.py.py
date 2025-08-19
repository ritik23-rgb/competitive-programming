
num = int(input("Enter a positive number: "))


if num > 0:
    print("The factorsare:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
else:
    print("Please enter a positive number!")
