# marks dictionary - average and subject with highest marks

physics = int(input("enter marks in physics: "))
chemistry = int(input("enter marks in chemistry: "))
maths = int(input("enter marks in maths: "))

marks = {
    "physics": physics,
    "chemistry": chemistry,
    "maths": maths
}

average = sum(marks.values()) / len(marks)
highest_subject = max(marks, key=marks.get)

print(f"average marks: {average:.2f}")
print(f"subject with highest marks: {highest_subject} ({marks[highest_subject]})")
