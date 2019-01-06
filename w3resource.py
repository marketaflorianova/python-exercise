# 4. Write a Python program which accepts the radius
# of a circle from the user and compute the area.

from math import pi

r = int(input("Insert the radius of your circle:"))

def area_of_circle(r):
    return pi*r**2
print("r = ", r, "\n area = ", area_of_circle(r))

# 5. Write a Python program which accepts the user's first
#  and last name and print them in reverse order with a
#  space between them.

given_name = input("Insert your given name: ")
surname = input("Insert your surname: ")

print(surname, " ", given_name)

# 6. Write a Python program which accepts a sequence
# of comma-separated numbers from user and
# generate a list and a tuple with those numbers.

numbers = input("Insert your numbers: ")

print(list(numbers.replace(", ","")))
print(tuple(numbers.replace(", ","")))

# 7. Write a Python program to accept a filename
# from the user and print the extension of that.

file = input("Insert the name of your file incl. its extension: ")
ending = file.split(".",1)[1]

print("Sample filename:", file, "\n extension:", ending)

# 8. Write a Python program to display the first
# and last colors from the following list.

colour_list = ["Red","Green","White" ,"Black"]

print(colour_list[0], colour_list[-1])


# 16. Write a Python program to get the difference between a given
# number and 17, if the number is greater than 17 return double
# the absolute difference.


number = int(input("Insert your number: "))

def difference(number):
    if number > 17:
        return 2*(abs(number - 17))
    else:
        return number - 17
print(difference(number))



# 20. Write a Python program to get a string which is
# n (non-negative integer) copies of a given string.

def repetition(n, word):
    return int(n)*(word + " ")
print(repetition(3, 'hello'))



# 24. Write a Python program to test whether a passed letter is a vowel or not

letter = input("Insert your letter: ")

def is_vowel(letter):
    vowels = 'aeiouy'
    if letter in vowels:
        return 'yes'
    else:
        return 'no'

print("Is the letter a vowel?", is_vowel(letter))


# 29. Write a Python program to print out a set
# containing all the colors from color_list_1
# which are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)


# 149. Write a Python function that takes a positive integer and returns the sum
# of the cube of all the positive integers smaller than the specified number.

a = int(input("Insert a number: "))
if a < 0:
    print("Please insert a positive integer!")

def cube(a):
    sum = 0
    for x in range(0, a):
        sum += x**3
    return sum
print(cube(a))


# 148. Write a Python function to find the maximum and minimum
# numbers from a sequence of numbers.

string = input("Insert a sequence of numbers divided by a space: ")
splitted_string = string.split()
listed_string = list(splitted_string)

intlist = map(int, listed_string)
sorted_intlist = sorted(intlist)

print(sorted_intlist)

print("Minimum is ", sorted_intlist[0],
"\n maximum is ", sorted_intlist[-1])



# 109. Write a Python program to check if a number is positive, negative or zero.

number = int(input("Insert a number: "))

def check(number):
    if number > 0:
        return 'positive'
    elif number < 0:
        return 'negative'
    else:
        return 'zero'
print(check(number))


# 1. Write a Python function that takes a sequence of numbers
# and determines if all the numbers are different from each other.

# string = input("Insert a sequence of numbers divided by a space: ")
# splitted_string = string.split()
# listed_string = list(splitted_string)
#
# intlist = map(int, listed_string)
# sorted_intlist = sorted(intlist)
#
# def difference(sorted_intlist):
#     for x in sorted_intlist:
#         if x - (x+1) > 0:
#             return "there are no duplicates in the sequence"
#         else:
#             return "there are duplicates in the sequence"
# print(difference(string))
# DOES NOT WORK - WHY?

string = input("Insert a sequence of numbers divided by a space: ")
splitted_string = string.split()
listed_string = list(splitted_string)

intlist = map(int, listed_string)
sorted_intlist = sorted(intlist)

print(sorted_intlist)

def difference(sorted_intlist):
    if len(sorted_intlist) == len(set(sorted_intlist)):
        return "there are no duplicates in the sequence"
    else:
        return "there are duplicates in the sequence"
print(difference(sorted_intlist))