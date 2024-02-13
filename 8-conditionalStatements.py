# SYNTAX -> if-elif-else

'''
if(condition):
    statement
elif(condition):
    statement2
else:
    statement3
'''

# else statement is optional and does not require a condition to be specified.

# Example ->
print("Example 1 (if-else) ->")
_age = int(input("Enter your age: "))

if(_age >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Example 2 ->
print("Example 2 (if-elif-else) ->")
_minAge = 18
_maxAge = 60
_userAge = int(input("Enter your age: "))

if(_userAge >= _minAge and _userAge <= _maxAge):
    print("You are eligible to work.")
    print("You can work for 8 hours a day.")
    print("You can drive.")
elif(_userAge < _minAge):
    print("You are not eligible to work.")
    print("You can't drive.")
else:
    print("You are too old to work.")
    print("You can't drive.")
    print("You can't work for more than 8 hours a day.")


# Nested if-else statement

'''
if(condition):
    if(condition):
        statement
    else:
        statement2
else:
    statement3
'''

# Example ->
# Check if a number is positive, negative or zero.
print("Example 3 (Nested if-else) ->")
_num = int(input("Enter a number: "))
if(_num > 0):
    print("The number is positive.")
elif(_num < 0):
    print("The number is negative.")
else:
    print("The number is zero.")


# Nested if-else statement

'''
if(condition):
    if(condition):
        statement
    else:
        statement2
else:
    if(condition):
        statement3
    else:
        statement4
'''

# Example ->
# Check if a number is positive, negative or zero.
print("Example 4 (Nested if-else) ->")
_num = int(input("Enter a number: "))
if(_num > 0):
    print("The number is positive.")
elif(_num < 0):
    print("The number is negative.")
else:
    if(_num == 0):
        print("The number is zero.")
    else:
        print("This is not a number.")



# Single line if / ternary operator

'''
SYNTAX: <variablt> = <value> if <condition> else <statement>

NOTE: You cannot use elif with this syntax.
'''

# Example ->
print("Example 5 (Single line if / ternary operator) ->")
_foodItem = "Pizza"
_wantToEat = "Yes" if _foodItem == "Pizza" else "I want to eat Pizza."
print(_wantToEat)

# Example 2 ->
# Check if a number is positive, negative or zero.
print("Example 6 (Single line if / ternary operator) ->")
_num = int(input("Enter a number: "))
_result = "The number is positive." if _num > 0 else "The number is negative." if _num < 0 else "The number is zero."


# Clever if statement

'''
SYNTAX: <variable> (false_value, true_value)[<condition>]
'''

# Example ->
# Check if a number is positive, negative or zero.
print("Example 7 (Clever if statement) ->")
_num = int(input("Enter a number: "))
_result = ("The number is negative.", "The number is positive.")[_num > 0]

# Example 2 ->
# Check if a number is positive, negative or zero.
print("Example 8 (Clever if statement) ->")
_num = int(input("Enter a number: "))
_result = ("The number is negative.", "The number is positive.", "The number is zero.")[_num < 0], [_num > 0], [_num == 0]

