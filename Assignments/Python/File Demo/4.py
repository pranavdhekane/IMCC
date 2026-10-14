with open("file.txt", "r") as f:
    content = f.read()

words = content.split()

print("Total number of words = ", len(words))

unique_words = set(words)
print("Total number of unique words = ", len(unique_words))