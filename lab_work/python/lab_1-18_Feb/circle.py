radius=float(input("Enter the radius of the circle_v2: "))
if radius <= 0:
    print("Invalid radius")
    exit()
else:
    pi=3.14159
    area=pi * radius * radius
    circumference=2 * pi * radius
    print("Area of the circle_v2 is:",area)
    print("Circumference of the circle_v2 is:",circumference)
