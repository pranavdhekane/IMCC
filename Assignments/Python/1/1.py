with open ('file.txt', 'r') as f:
    students = f.readlines()

students = [x.strip() for x in students]
print(students)