# Q40. Design a mini student management system using functions, dictionaries, 
# file handling, exception handling, and Pandas for report generation.

import pandas as pd
import json

class StudentManagementSystem:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = {}
        self.load_data()
        
    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.students = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = {}
            
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f)
            
    def add_student(self, roll_no, name, marks):
        self.students[str(roll_no)] = {'name': name, 'marks': marks}
        self.save_data()
        print(f"Added student {name}.")
        
    def generate_report(self):
        if not self.students:
            print("No student data available.")
            return
            
        # Convert nested dictionary to a list of dicts for Pandas
        data = [{'RollNo': k, 'Name': v['name'], 'Marks': v['marks']} 
                for k, v in self.students.items()]
                
        df = pd.DataFrame(data)
        df['Status'] = df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
        print("\n--- Student Report ---")
        print(df.to_string(index=False))

if __name__ == "__main__":
    sms = StudentManagementSystem('test_students.json')
    sms.add_student(101, "Alice", 85)
    sms.add_student(102, "Bob", 35)
    sms.generate_report()

# Expected Output:
# Added student Alice.
# Added student Bob.
# 
# --- Student Report ---
# RollNo   Name  Marks Status
#    101  Alice     85   Pass
#    102    Bob     35   Fail
