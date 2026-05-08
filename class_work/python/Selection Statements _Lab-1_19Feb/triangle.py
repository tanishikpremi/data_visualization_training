angle1 = int(input("Enter the value for angle 1:"))
angle2 = int(input("Enter the value for angle 2:"))
angle3 = int(input("Enter the value for angle 3:"))

if (angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0):
    print("These angles forn a triangle")
else:
    print("Triangle is not possible")