with open('file.txt', 'r') as f:
    students = f.readlines()
    
students = [student.strip() for student in students]
students = filter(lambda x: len(x)> 5, students)

with open('students.txt', 'w') as f2:
    for i in students:
        f2.write(i + "\n")
    
    