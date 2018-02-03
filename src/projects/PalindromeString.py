# check if a string is a palindrome
word = str(input("Please enter a word "))
reversedWord = word[::-1]
print(reversedWord)
if word == reversedWord:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
