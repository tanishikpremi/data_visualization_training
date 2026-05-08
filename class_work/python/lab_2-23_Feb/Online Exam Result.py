def process_exam_results(scores):
    # Remove lowest 2 scores
    scores.sort()
    trimmed_scores = scores[2:]
    
    # Add grace marks of 5 to those scoring between 30-35
    final_scores = [s + 5 if 30 <= s <= 35 else s for s in trimmed_scores]
    
    # Count number of students passed (>= 40)
    passed_count = sum(1 for s in final_scores if s >= 40)
    
    print(f"Final Scores (after removing lowest 2 & grace marks): {final_scores}")
    print(f"Number of Students Passed: {passed_count}")

# Test
process_exam_results([25, 88, 32, 14, 45, 39, 34, 90])