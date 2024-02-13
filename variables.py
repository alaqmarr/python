# Like in C language we use // to write a comment, in Python we use # to write a comment.
# The comment is a line of text that is not executed by the program.
# Like in C language we have variables, in Python we have variables but in python we don't need to declare the type of the variable.
# The variable is a container to store data.
# The data is the information.
# The information is the input to the computer program.
# The input is the data to be processed.
# The data to be processed is the data to be manipulated.

# Examples of variables in Python:

name = "Al Aqmar"
age = 20
contact_number = 9618443558
contact_email = "alaqmarak0810@gmail.com"
college = "Swami Vivekanand Institute of Technology (SVIT)"
course_duration = "4 years"
batch = "2023 - 2027"

# In the above example, name, age, college, course_duration, and batch are variables.

# Now, let's see how to display the output of these variables.

# Like in C language we used printf("d",age) to display the value of the variable age, in Python we use print(age) to display the value of the variable age.

# Also in Python we do not use ; to end a statement like in C language. The statement ends when the line ends.

print(name)
print(age)
print(contact_number)
print(contact_email)
print(college)
print(course_duration)
print(batch)

# The variabeles can be converted to any other data type using two techniques: 1: Using Type Conversion (this is called Explicit Type Conversion) 2: Using Type Casting (this is called Implicit Type Conversion)

# Type Conversion: This is done by the machine itself. We don't need to do anything. The machine will automatically convert the data type of the variable to the required data type.

# Type Casting: This is done by the programmer. We need to write the code to convert the data type of the variable to the required data type. The function used is called the casting function. "str(age)" is an example of type casting. Here, the data type of the variable age is converted to a string data type.

str_age = str(age)
print(str_age)

# In the above example, the data type of the variable age is converted to a string data type.

# We use type() to check the data type of the variable. If the data type of the variable is a string, the output will be <class 'str'>. If the data type of the variable is an integer, the output will be <class 'int'> and so on.

print(type(name))
print(type(age))
print(type(contact_number))
print(type(contact_email))
print(type(college))
print(type(course_duration))
print(type(batch))
print(type(str_age))

# In the above example, the data type of the variable name is a string, the data type of the variable age is an integer, the data type of the variable contact_number is an integer, the data type of the variable contact_email is a string, the data type of the variable college is a string, the data type of the variable course_duration is a string, the data type of the variable batch is a string, and the data type of the variable str_age is a string.