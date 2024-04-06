# If a number is prime or not
number = int(input("Enter a number: ")) # 10

for i in range(2, number): # 2 - 9
    if (number % i == 0): # 13 % 2 = 1, 13 % 3 = 1, 13 % 4 = 1, 13 % 12 = 1
        print("Not a prime")
        break
else:
    print("A prime")