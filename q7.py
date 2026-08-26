word = input("enter a word: ")
reversed = ""
for ch in word:
    reversed = ch + reversed
print("reversed word:", reversed)
