# multiplication table (1 to 10) of a number

num = int(input("input a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
