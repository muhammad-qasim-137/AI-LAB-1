# marks of 3 subjects - average and percentage using dictionary

sub1 = input("enter name of subject 1: ")
marks1 = float(input(f"enter marks in {sub1}: "))
sub2 = input("enter name of subject 2: ")
marks2 = float(input(f"enter marks in {sub2}: "))
sub3 = input("enter name of subject 3: ")
marks3 = float(input(f"enter marks in {sub3}: "))

marks_dict = {
    sub1: marks1,
    sub2: marks2,
    sub3: marks3
}

total = sum(marks_dict.values())
average = total / len(marks_dict)
percentage = (total / (len(marks_dict) * 100)) * 100  # assuming each subject is out of 100

print("marks dictionary:", marks_dict)
print(f"average: {average:.2f}")
print(f"percentage: {percentage:.2f}%")
