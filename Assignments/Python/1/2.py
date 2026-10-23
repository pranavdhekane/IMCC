with open ('file.txt', 'r') as f:
    students = f.readlines()
   
students = [x.strip() for x in students]

for i in students:
    if len(i) > 5:
        print(i)