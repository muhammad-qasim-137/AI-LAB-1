c = int(input("enter number of members in list: "))
nums = [0]*c
highest = 0
for i in range(c):
    nums[i] = int(input("enter number: "))
    if nums[i] > highest:
      highest = nums[i]
print("largest number:",highest)
