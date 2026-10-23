def isPalindrome(s):
    s = s.lower()
    return s == s[::-1]

with open("file.txt", "r") as f:
    students = f.readlines()

students = [student.strip() for student in students]

for i in students:
    print(f"Length of {i}: {len(i)}")    
    print(f"Name {i} is {'a' if isPalindrome(i) else 'not a'} palindrome")
    print(f"First Letter {i[0]} and Last Letter {i[-1]}")
    print()
