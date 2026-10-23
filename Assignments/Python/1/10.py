with open("file.txt", "r") as f:
    students = f.readlines()

students = [student.strip() for student in students]

d = dict()
for i in students:
    if i[0] in d:
        d[i[0]].append(i)
    else:
        d[i[0]] = [i]

for i, names in d.items():
    with open(f"{i.upper()}_names.txt", "w") as f:
        for name in names:
            f.write(name + "\n")

    