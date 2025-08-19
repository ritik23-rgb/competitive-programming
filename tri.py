#Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle)
a = int(input("enter angle A :"))
b = int(input("enter angle C :"))
c = int(input("enter angle B :"))

if a+b+c == 180:
    if a==90 or b==90 or c==90:
        print("right angle triagle")
    elif a>90 or b>90 or c>90:
        print("obtuse triangle ")
    else:
        print("acute triangle")
else:
    print("enter valid angles")
