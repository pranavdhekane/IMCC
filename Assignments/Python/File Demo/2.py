with open("file.txt", "r") as f:
    lines = f.readlines()

print("Total number of lines = ", len(lines))

if len(lines) >= 4:
    print("The 2nd line is: ", lines[1])
    print("The 4th line is: ", lines[3])
else:
    print("The file has less than 4 lines.")