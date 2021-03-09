#task6 Palindrome


word = input("State a word for Palindrome test: ")
word = str(word)
wordReverse = str()
palindrome = False

wordReverse=word[::-1]
print(wordReverse)
if word == wordReverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
    print(wordReverse)
