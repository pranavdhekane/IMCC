line = input("Enter a sentence: ")
words = line.split(" ")

maxlen = 0
maxWord = ""

for i in words:
    if maxlen < len(i):
        maxlen = len(i)
        maxWord = i

print(f"Longest word = {maxWord} with length = {maxlen}")