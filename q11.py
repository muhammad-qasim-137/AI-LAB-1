sub1 = input("enter name of subject 1: ")
marks1 = float(input(f"enter marks in {sub1}: "))
sub2 = input("enter name of subject 2: ")
marks2 = float(input(f"enter marks in {sub2}: "))
sub3 = input("enter name of subject 3: ")
marks3 = float(input(f"enter marks in {sub3}: "))
marksdict = {
    sub1: marks1,
    sub2: marks2,
    sub3: marks3
}
total = 0
for subject in marksdict:
    total += marksdict[subject]

average = total / len(marksdict)
percentage = (total / (len(marksdict) * 100)) * 100

print("marks dictionary:", marksdict)
print(f"average: {average}")
print(f"percentage: {percentage}%")
