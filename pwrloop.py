# solve a**b using for loop.
a = int(input("enter a  "))
b = int(input("enter b  "))
rslt = 1
for i in range(b):
    rslt *= a
print(rslt)