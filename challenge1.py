# count vowels (a, e, i, o, u) and consonants (all other letters) in a string 
# count the number of capital / upper case letters
# remove spaces from string without string methods

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

num_vowels = 0
num_consonants = 0
num_upper_case = 0

for character in sentence:

    if character.isupper():
        num_upper_case += 1

    if character in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ':
        continue

    if character.lower() in 'aeiou':
        num_vowels += 1
    else:
        num_consonants += 1


print(f"Number of vowels: {num_vowels}")
print(f"Number of consonants: {num_consonants}")
print(f"Number of upper case characters: {num_upper_case}")

sentence_without_space = ""

for character in sentence:
    if character != " ":
        sentence_without_space += character

print(sentence_without_space)