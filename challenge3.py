# palindrome

# string reversed is also the same as the original string

# firetruck = kcurterif -> not a palindrome
# racecar = racecar -> palindrome

original_string = "fwquhydaisu"

reversed_string = ""

for character in original_string: # f, i, r, e
    reversed_string = character + reversed_string # f, if, rif, erif

print(reversed_string)

if (reversed_string == original_string):
    print("A palindrome")
else:
    print("Not a palindrome")

print("A palindrome") if reversed_string == original_string else print("Not a palindrome")