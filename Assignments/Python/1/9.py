with open("file.txt", "r") as f:
    students = f.readlines()

students = [student.strip() for student in students]

distinct_students = list(set(students))

for i in range(len(distinct_students)):
    for j in range(i + 1, len(distinct_students)):
        if len(distinct_students[i]) > len(distinct_students[j]):
            distinct_students[i], distinct_students[j] = distinct_students[j], distinct_students[i]

with open("processed_names.txt", "w") as f:
    for student in distinct_students:
        f.write(student + "\n")