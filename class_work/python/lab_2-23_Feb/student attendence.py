def track_attendance(attendance):
    # Calculate attendance percentage
    total_days = len(attendance)
    days_present = sum(attendance)
    percentage = (days_present / total_days) * 100
    
    print(f"Attendance Percentage: {percentage:.2f}%")
    
    # Identify if below 75%
    if percentage < 75:
        print("Alert: Attendance is below 75%!")
        
    # Replace consecutive absences (0, 0) with a warning flag
    processed_attendance = []
    i = 0
    while i < len(attendance):
        if i < len(attendance) - 1 and attendance[i] == 0 and attendance[i+1] == 0:
            processed_attendance.append("Warning")
            i += 2 # Skip the next zero since it's part of the consecutive absence
        else:
            processed_attendance.append(attendance[i])
            i += 1
            
    print(f"Processed Attendance: {processed_attendance}")

# Test
track_attendance([1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0])