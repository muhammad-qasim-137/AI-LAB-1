value = float(input("enter the number: "))
c = int(input("enter number of members in list: "))
nums = [0]*c
for i in range(c):
    nums[i] = int(input("enter number: "))
    if(nums[i]<value):
        nums[i] = 0
print(nums)
