# Strings and Numeric values can operate together with '*'.
a,b=2,3
text="."
print(a*text*b)
# In this snippet, we are using the * operator to print the value of a and b. The output will be: .....


# Strings and Strings can operate together with '+'.
text1="Hello"
text2="World"
text3="!"
print(text1+text2+text3)
# In this snippet, we are using the + operator to print the value of text1 and text2. The output will be: HelloWorld!


# Numeric values can operate together with all the arithmetic operators.
A,B=5,2
C=10
print(A+B*C)
# In this snippet, we are using the + and * operator to print the value of A, B and C. The output will be: 25

# Arithmetic operations with integers and floats will result in a float value as the output.
# Result of the division operation will always be a float value.
# Integer division will result in a float value.
# Integer division is performed using the // operator.

# floor gives closest integer value which is less than or equal to the float value.

# Result of (A//B) is same as floor(A/B).
# Result of (A%B) is same as A-(B*(A//B)).
# Result of (A**B) is same as A raised to the power B.
# Result of (A**0.5) is same as square root of A.
# Result of (A**-1) is same as 1/A.


# Remainder will be nagative if the denominator is negative.
'''
if {N-> +ve, D-> +ve} then R-> +ve
if {N-> -ve, D-> +ve} then R-> +ve
if {N-> +ve, D-> -ve} then R-> -ve
if {N-> -ve, D-> -ve} then R-> +ve
NOTE: This is applicable for both modulus division.
'''