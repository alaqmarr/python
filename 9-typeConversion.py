# TYPE CONVERSION

a1,b1 = 10,20.0
c1 = a1 + b1
print(c1)
# In the above code snippet, the value of a is 10 and the value of b is 20.0. The value of c is the sum of a and b. The value of a is an integer and the value of b is a float. The value of c is the sum of an integer and a float. The value of c is 30.0. The type of c is float. Hence, the output is 30.0.

# NOTE : You cannot add string and integer or string and float.

a2="2"
b2=2
c2=a2+b2
print(c2)
# The Above code snippet will give an ERROR because you cannot add string and integer.

'''
There are two types of type conversion in Python:

1-> Implicit Type Conversion -> Type Conversion -> In this case the data type is automatically converted by Python.


2-> Explicit Type Conversion -> Type Casting -> In this case the data type has to be manually converted by the programmer. This action cannot be done by Python itself.
'''

# Type Casting

a3=10
b3='2'
c3 = int(b3) # here we are forcefully converting the string to integer
d3 = a3 + c3
print(d3)
# In the above code snippet, the value of a is 10 and the value of b is '2'. The value of c is the integer value of b. The value of c is 2. The value of d is the sum of a and c. The value of d is 12. The type of d is integer. Hence, the output is 12.

# NOTE : Type casting will only work if the string is a number. If the string is a character, then it will give an error but we can convert an integer to a string.