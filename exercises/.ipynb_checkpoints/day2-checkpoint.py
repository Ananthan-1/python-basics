# 1. Given a list of numbers, create a new list with each number squared (use list comprehension).
nums=[1,2,3,4,5,6,7,8,9,10]
squares=[x*x for x in nums]
print(squares)

# 2. Given a list of strings, return only the strings with length > 3.
list1=["Clever","Ant","Dog","Glory","An"]
result=[i for i in lsit1 if len(i)>3]
print(result)      

# 3. Create a dictionary for 3 students and their scores.
#    Print the student who has the highest score.
students={
    "Ron":98,
    "Craig":88,
    "Jan":97}
hscore=max(students,key=students.get)
print("HIGHEST SCORE:",hscore,students[hscore])

# 4. Read Sample text and print each line with its line number.
with open("D:/STUDY/python-basics/data/day2_sampletext.txt","r") as f:
    for line_num,line in enumerate(f,start=1):
        print(f"{line_num}:{line.strip()}")


# 5. Append a new line to the text
text_append="THIS IS A NEW LINE APPENDED"
with open("D:/STUDY/python-basics/data/day2_sampletext.txt","a") as f:
    file.write("\n"+text_append)