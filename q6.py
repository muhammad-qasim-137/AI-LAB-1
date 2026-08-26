physics = int(input("enter marks in physics: "))
chemistry = int(input("enter marks in chemistry: "))
maths = int(input("enter marks in maths: "))
marks = {
    "physics": physics,
    "chemistry": chemistry,
    "maths": maths
}
total = 0
for subject in marks:
    total += marks[subject]
average = total / len(marks)
highest = ""
highmarks = -1
for subject in marks:
    if marks[subject] > highmarks:
        highmarks = marks[subject]
        highest = subject

print(f"average marks: {average}")
print(f"subject with highest marks: {highest} ({marks[highest]})")
