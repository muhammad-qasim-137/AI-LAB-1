# reverse a word using a loop

word = input("enter a word: ")
reversed_word = ""

for ch in word:
    reversed_word = ch + reversed_word

print("reversed word:", reversed_word)
