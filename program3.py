# count even numbers in a list

nums = list(map(int, input("enter integers separated by spaces: ").split()))
count = 0

for n in nums:
    if n % 2 == 0:
        count += 1

print("count of even numbers:", count)
