with open("file.txt", "r") as f:
    students = f.readlines()

students = [student.strip() for student in students]

d = dict()
for i in students:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for student, count in d.items():
    print(f"{student}: {count}")