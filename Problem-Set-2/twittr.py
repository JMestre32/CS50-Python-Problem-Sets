# without_vowels = input("Input: ")

# without_vowels = without_vowels.replace("A", "")
# without_vowels = without_vowels.replace("a", "")
# without_vowels = without_vowels.replace("E", "")
# without_vowels = without_vowels.replace("e", "")
# without_vowels = without_vowels.replace("I", "")
# without_vowels = without_vowels.replace("i", "")
# without_vowels = without_vowels.replace("O", "")
# without_vowels = without_vowels.replace("o", "")
# without_vowels = without_vowels.replace("U", "")
# without_vowels = without_vowels.replace("u", "")

# print("Output: " + without_vowels)


#This was pretty brute force, but it got the job done. In order solve this
#via loops you would do something like this:

without_vowels = input("Input: ")

print("Output: ", end="")
 #Loop through each letter
for letter in without_vowels:
    if not letter in ['a', 'e', 'i', 'o', 'u']:
        print(letter, end ="")
print()