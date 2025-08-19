#15. Accept the percentage from the user and display the grade according to the following criteria. ●Below 25 – D ●25 to 45 – C ●45 to 65 – B ●65 to 85 – A ●Above 85 – A+

p = int(input("entr percentage: "))
if p < 25:
    print("D")
elif p > 25 & marks <45:
    print("C")
elif p > 45 & marks < 65:
    print("B")
elif p > 65 & marks < 85:
    print("A")
elif p > 85:
    print("A+")
else:
    print("Invalid marks entered.")
