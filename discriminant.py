import math
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
d = math.pow(b, 2) - 4*a*c
if d > 0:
    x1 = ((-b) - math.sqrt(d)) / 2*a
    x2 = ((-b) + math.sqrt(d)) / 2*a
    print()
    print(f"x1 = {x1} \nx2 = {x2}")
elif d == 0:
    x = (-b) / 2*a
    print()
    print(f"x = {x}")
else:
    print()
    print("No solution")