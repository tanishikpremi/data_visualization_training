def monitor_temperatures(temps):
    # Find hottest and coldest day
    hottest = max(temps)
    coldest = min(temps)
    
    # Count extreme days (> 40°C) BEFORE replacing integers with strings
    extreme_days = sum(1 for t in temps if t > 40)
    
    # Replace temperatures above 45°C with "Heat Alert"
    processed_temps = ["Heat Alert" if t > 45 else t for t in temps]
    
    print(f"Hottest Day: {hottest}°C, Coldest Day: {coldest}°C")
    print(f"Number of Extreme Days (>40°C): {extreme_days}")
    print(f"Processed Log: {processed_temps}")

# Test
monitor_temperatures([35, 38, 42, 46, 39, 41, 48])