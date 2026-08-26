c = int(input("enter number of members in list: "))
nums = [0]*c
for i in range(c):
    nums[i] = int(input("enter number: "))
count = 0
for n in nums:
    if n % 2 == 0:
        count += 1
print("count of even numbers:", count)
