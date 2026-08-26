# delete all elements in list less than a given number

nums = list(map(float, input("enter numbers separated by spaces: ").split()))
threshold = float(input("enter the number: "))

nums = [n for n in nums if n >= threshold]

print("list after deletion:", nums)
