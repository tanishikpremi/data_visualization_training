def process_tournament(points):
    # Replace negative points with 0
    valid_points = [0 if p < 0 else p for p in points]
    
    # Sort leaderboard (descending order for highest points)
    valid_points.sort(reverse=True)
    
    # Find winner and runner-up
    winner = valid_points[0] if len(valid_points) > 0 else None
    runner_up = valid_points[1] if len(valid_points) > 1 else None
    
    print(f"Sorted Leaderboard: {valid_points}")
    print(f"Winner Points: {winner}")
    print(f"Runner-up Points: {runner_up}")

# Test
process_tournament([15, -3, 22, 18, 5, -1])