with open('file.txt', 'r') as file:
    students = file.readlines()

students = [student.strip() for student in students]
studentsWithLetterA = list(filter(lambda x: 'a' in x.lower(), students))

for i in studentsWithLetterA:
    print(i)