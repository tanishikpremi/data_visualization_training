def process_ratings(ratings):
    # Remove invalid ratings
    valid_ratings = [r for r in ratings if 1 <= r <= 5]
    
    if not valid_ratings:
        return "No valid ratings."
        
    # Find average rating
    average = sum(valid_ratings) / len(valid_ratings)
    
    # Count how many 5-star ratings
    five_stars = valid_ratings.count(5)
    
    # Sort ratings in ascending order
    valid_ratings.sort()
    
    print(f"Sorted Valid Ratings: {valid_ratings}")
    print(f"Average Rating: {average:.1f}")
    print(f"5-Star Ratings Count: {five_stars}")

# Test
process_ratings([4, 6, 2, 5, 1, -2, 5, 3])