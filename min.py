# 14. Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C

a = int(input("enter number A : "))
b = int(input("enter number B : "))
c = int(input("enter number c : "))
if a<b and a<c :
    print("a is minimum ")
elif b<a and b<c :
    print("b is min. ")
else :
    print ("c is min.")
