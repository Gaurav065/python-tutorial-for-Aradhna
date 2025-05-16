# Initialize an empty list to store student records
records = []

# Read the data from the file
with open(r'File_handeling\tutorial.txt', 'r') as file: 
    for line in file:
        name, subject, marks = line.strip().split(',')
        records.append({'name': name, 'subject': subject, 'marks': int(marks)})

# Function to calculate average marks
def calculate_average_marks(records):   
    total_marks = sum(record['marks'] for record in records)
    num_records = len(records)
    average_marks = total_marks / num_records if num_records != 0 else 0
    return average_marks

# Example usage
average = calculate_average_marks(records)
print("Average Marks:", average)
