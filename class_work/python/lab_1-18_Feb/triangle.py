angle1=float(input("Enter first angle: "))
if angle1 <= 0:
    print("Invalid angle")
    exit()
else:
    angle2=float(input("Enter second angle: "))
    if angle2 <= 0:
        print("Invalid angle")
        exit()
    else:
        angle3=float(input("Enter third angle: "))
        if angle3 <= 0:
            print("Invalid angle")
            exit()
        elif angle1 + angle2 + angle3 == 180:
            print("The three angles can form a triangle_v2")
        else:
            print("The three angles cannot form a triangle_v2")
