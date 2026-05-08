second=int(input("Enter time in seconds: "))
minutes=0
hours=0
if second >= 3600:
    hours=second
    second=second % 3600
if second >= 60:
    minutes=second
    second=second % 60
print("Time in hours: ",hours)
print("Time in minutes: ",minutes)
print("Time in seconds: ",second)
