with open("file.txt", "r") as f:
    line = f.read()

count = 0
s = {"a", "e", "i", "o", "u"}

for i in line.lower():
    if i in s:
        count += 1

print(f"Number of vowels = {count}")