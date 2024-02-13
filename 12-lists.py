# LISTS IN PYTHON

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

marks = [10, 20, 30, 40, 50]
print(marks)
# This will print [10, 20, 30, 40, 50]

'''
Rules in creating a list:
1-> The list is written with square brackets.
2-> Items are separated by commas.
3-> Items are ordered, changeable, and allow duplicate values.
4-> List items are indexed, the first item has index [0], the second item has index [1] etc.
5-> When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
6-> Lists are changeable, meaning that we can change, add, and remove items in a list after it has been created.
7-> Since lists are indexed, lists can have items with the same value.
'''

'''
Indexing in lists:
1-> We can access the list items by referring to the index number.
2-> The index must be in square brackets.
3-> The index starts at 0.
4-> Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
'''

# Store elements of different types in a list
profile = ["Al Aqmar", 20, 9618443558, "SVIT"]
print(profile)
# This will print ['Al Aqmar', 20, 9618443558, 'SVIT']

# Accessing elements of a list
print(profile[0])
# This will print Al Aqmar
print(profile[-1])
# This will print SVIT

# Slicing of a list
print(profile[1:3])
# This will print [20, 9618443558]

# Change the value of a list item
profile[1] = 21
print(profile)
# This will print ['Al Aqmar', 21, 9618443558, 'SVIT']

# Loop through a list
for x in profile:
    print(x)
# This will print:
# Al Aqmar
# 21
# 9618443558
# SVIT

# Check if an item exists in a list
if 21 in profile:
    print("Yes, 21 is in the list")
# This will print Yes, 21 is in the list

# Find the length of a list
print(len(profile))
# This will print 4

# Add items to a list
profile.append("CSE")
print(profile)
# This will print ['Al Aqmar', 21, 9618443558, 'SVIT', 'CSE']

# Insert items to a list
profile.insert(1, "Student")
print(profile)
# This will print ['Al Aqmar', 'Student', 21, 9618443558, 'SVIT', 'CSE']

# Remove items from a list
profile.remove("Student")
print(profile)
# This will print ['Al Aqmar', 21, 9618443558, 'SVIT', 'CSE']

# Remove items from a specific index
profile.pop(1)
print(profile)
# This will print ['Al Aqmar', 9618443558, 'SVIT', 'CSE']


'''
Methods in lists:
1-> append(value) - Adds an element at the end of the list
2-> insert(index, value) - Adds an element at the specified position
3-> remove(value) - Removes the first item with the specified value
4-> pop(index) - Removes the element at the specified position
5-> clear() - Removes all the elements from the list
6-> copy() - Returns a copy of the list
7-> count(value) - Returns the number of elements with the specified value
8-> index(value) - Returns the index of the first element with the specified value
9-> reverse() - Reverses the order of the list
10-> sort() - Sorts the list : sort(reverse=True) will sort the list in descending order
'''

# Ask user to input their 3 favpurite movies and store as a list

movies = []
movie1 = input("Enter your first favourite movie: ")
movies.append(movie1)
movie2 = input("Enter your second favourite movie: ")
movies.append(movie2)
movie3 = input("Enter your third favourite movie: ")
movies.append(movie3)
print(movies)
# This will print the list of movies entered by the user

            # OR

movies = []
for i in range(3):
    movie = input("Enter your favourite movie: ")
    movies.append(movie)
print(movies)
# This will print the list of movies entered by the user

        # OR

movies = []
movies.append(input("Enter your first favourite movie: "))
movies.append(input("Enter your second favourite movie: "))
movies.append(input("Enter your third favourite movie: "))
print(movies)
# This will print the list of movies entered by the user

        # OR

movies = [input("Enter your first favourite movie: "), input("Enter your second favourite movie: "), input("Enter your third favourite movie: ")]
print(movies)

        # OR

movies = [input("Enter your favourite movie: ") for i in range(3)]


# Write a program to check is a list contains a palindrome of elements.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
# For example: radar, 12321, 123321

# Using copy() and reverse() method
a = [1, 2, 3, 4, 5]
b = a.copy()
b.reverse()
if a == b:
    print("Palindrome")
else:
    print("Not a palindrome")


# Method 1
def is_palindrome(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst)-1-i]:
            return False
    return True

print(is_palindrome([1, 2, 3, 2, 1]))
# This will print True


# Method 2
def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))
# This will print True


# Method 3
def is_palindrome(lst):
    return lst == list(reversed(lst))

print(is_palindrome([1, 2, 3, 2, 1]))
# This will print True
