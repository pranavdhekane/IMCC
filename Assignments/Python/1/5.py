with open('file.txt', 'r') as f:
    students = f.readlines()

students = [student.strip() for student in students]

for i in range(len(students)):
    for j in range(i+1, len(students)):
        if students[i] > students[j]:
            students[i], students[j] = students[j], students[i]

for i in students:
    print(i)