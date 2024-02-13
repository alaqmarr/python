# A variable is a name given to a memory location.
# A variable is used to store / access / manipulate data in the memory.
# Python is a Typed Language.
# Python is a implicitly typed language. We don't need to specify the data type of the variable. Python automatically assigns the data type to the variable based on the value assigned to it.

name = "Al Aqmar"
age = 20
contact_number = 9618443558
contact_email = "alaqmarak0810@gmail.com"
course = "B.Tech Computer Science Engineering"
course_duration = 4
college = "Swami Vivekananda Institute of Technology"

# Above we have created 7 variables. The variables are name, age, contact_number, contact_email, course, course_duration, college.
# "name" is the name of the variable and "Al Aqmar" is the value of the variable.

print(name)
print(age)
# and so on...
# We can print the value of the variable by passing the variable as the input to the print function.
# NOTE: We don't need to use "" for the variable name. We use "" for the value of the variable.

print("My name is", name)
# We can also print the value of the variable along with the string by using the variable as the input to the print function.
# The output will be: My name is Al Aqmar

age2 = age
# We can also assign the value of one variable to another variable.

''' Rules for Identifiers:
    1. Identifiers can be a combination of letters in lowercase (a-z) or uppercase (A-Z) or digits (0-9) or an underscore (_).
    2. An identifier cannot start with a digit.
    3. Keywords cannot be used as identifiers.
    4. We cannot use special symbols in the identifier name.
    5. An identifier can be of any length.
    6. Identifiers are case-sensitive.
    7. Identifiers should be meaningful.
'''

print(type(name))
# We can check the type of the variable by using the type function.
# The output will be: <class 'str'>
# str is the data type of the variable name.

# Data Types in Python: String, Integer, Float, Complex, Boolean, None, List, Tuple, Set, Dictionary, etc.
