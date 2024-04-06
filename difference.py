# numbers are primitive data types

num1 = 5 # assigns 5 to num1

num2 = num1 # assigned the value of num1 to num2 # copies the data by value

num1 = 10 # changed the value of num1 to 10

print(num1)
print(num2)


list1 = [ 1, 2, 3, 4 ] # assign [] to list1

list2 = list1 # assign list1 to list2 # copy by reference - copy by address

list3 = list1.copy()

list1.append(5) # change something in list1

print(list1)
print(list2)
print(list3)