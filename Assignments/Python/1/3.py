with open('file.txt', 'r') as f:
    students = f.readlines()
    
vow = {'a', 'e', 'i', 'o', 'u'}
count = 0
for i in students:
    if i[0].lower() in vow:
        count += 1
        
print(f"{count} students name starts with vowels")