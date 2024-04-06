# Non-primitive data types - hold/store multiple pieces of data

# List - Array - collection of data - indexed - mutable (changed)
numbers = [ 13, 2, 5, 98, 56 ]
#           0   1  2  3   4

print(numbers)
print(numbers [2])

numbers[2] = 10
print(numbers)

numbers.append(42)
print(numbers)

numbers.insert(2, 16)
print(numbers)

numbers.pop()
print(numbers)

numbers.remove(98)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers)) #len = length

# index, count

print("\n")

# Tuple - collection of data - indexed - immutable (cannot be changed)

# () - small brackets - parentheses
# {} - curly brackets - curly brackets
# [] - big brackets - square brackets

names = ( "John", "Jane", "Mike", "Jane", "Jane" )
#           0       1       2

print(names)
print(names[1])
# names[2] = "Steve" - Does not work
# names.append("Steve") - Does not work
print(len(names))
print(names.count("Jane"))
print(names.count("Mike"))

days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
co_ordinates_of_some_famous_place = (123.56, 20.2)


