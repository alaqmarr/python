# TUPLES IN PYTHON

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Items are separated by commas.
# Tuples are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add, or remove items after the tuple has been created.

tup = (10, 20, 30, 40, 50)
print(tup)
# This will print (10, 20, 30, 40, 50)

print(tup[0])
# This will print 10

# tup[0] = 5, This is not allowed as tuples are unchangeable

tup1 = (1,)
print(tup1)
# This will print (1,)
# For single values, If we do not use a comma, Python will not recognize it as a tuple

'''
Rules in creating a tuple:
1-> The tuple is written with round brackets.
2-> Items are separated by commas.
3-> Items are ordered, unchangeable, and allow duplicate values.
4-> Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
5-> When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
6-> Tuples are unchangeable, meaning that we cannot change, add, or remove items after the tuple has been created.
7-> Since tuples are indexed, tuples can have items with the same value.
'''

'''
Operations on tuples:
1-> Length of a tuple
2-> Concatenation of tuples
3-> Repetition of tuples
4-> Membership in a tuple
5-> Iteration through a tuple
6-> Indexing
7-> Slicing
'''

# TUPLE METHODS

# tup.index(element) -> This will return the index of the first occurrence of the element.
# tup.count(element) -> This will return the number of occurrences of the element.