is_raining = input("Is it raining? Yes or No?: ")

# if is_raining:
#     print("I need an umbrella")
# else:
#     print("I don't need an umbrella")

# Ternary Operator
# <statement to execute when true> if <condition> else <statement to execute when false>

print("You need an umbrella") if is_raining == "No" else print("You don't need an umbrella")
