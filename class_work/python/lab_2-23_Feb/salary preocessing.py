def process_salaries(salaries, min_wage=15000):
    # Remove salaries below minimum wage
    valid_salaries = [s for s in salaries if s >= min_wage]
    
    # Add 5% bonus to employees with salary > 50,000
    updated_salaries = [s * 1.05 if s > 50000 else s for s in valid_salaries]
    
    # Sort salaries in descending order
    updated_salaries.sort(reverse=True)
    
    # Display top 3 highest salaries
    top_3 = updated_salaries[:3]
    
    print(f"Processed & Sorted Salaries: {updated_salaries}")
    print(f"Top 3 Highest Salaries: {top_3}")

process_salaries([12000, 45000, 60000, 18000, 80000, 55000])