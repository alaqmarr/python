# String is a data type that is used to store a sequence of characters. In Python, a string is a sequence of Unicode characters. It is immutable. This means that once a string is created, it cannot be changed. Strings are used to store text. In Python, strings are enclosed in either single quotes or double quotes. For example, 'Hello' and "Hello" are both strings.
# Strings can be created using single / double / triple quotes. For example:
# Single Quotes -> 'Hello'
# Double Quotes -> "Hello"
# Triple Quotes -> '''Hello''' or """Hello"""

name = "Al Aqmar"
# This is a string

title = "Mr."

# CONCATENATION ->
_nameWithTitle = title + " " + name;
print(_nameWithTitle)

# This will add the title and name together and will give the output as "Mr. Al Aqmar"


# LENGTH OF A STRING ->
_lenth = len(_nameWithTitle)
print(_lenth)

# This will give the length of the string _nameWithTitle which is 10


# INDEXING ->
_index = _nameWithTitle[0]
print(_index)

# This will give the first character of the string _nameWithTitle which is "M". Indexing in Python starts from 0.
# NOTE : _nameWithTitle[0] = 'a' is not possible as the string is immutable. It cannot be manipulated.


# SLICING ->
_slice = _nameWithTitle[0:3]
print(_slice)

# This will give the first 3 characters of the string _nameWithTitle which is "Mr."
'''
Rules for Slicing ->
1) The first index is inclusive and the second index is exclusive.
2) If the first index is not given, it is considered as 0.
3) If the second index is not given, it is considered as the length of the string.
4) If the first index is greater than the second index, the result will be an empty string.
5) If the first index is greater than the length of the string, the result will be an empty string.
6) If the second index is greater than the length of the string, it is considered as the length of the string.
'''

# NEGATIVE INDEX SLICING ->
_negativeSlice = _nameWithTitle[-3:]
print(_negativeSlice)

# This will give the last 3 characters of the string _nameWithTitle which is "mar"
'''
Rules for Negative Index Slicing ->
1) The first index is inclusive and the second index is exclusive.
2) If the first index is not given, it is considered as -1.
3) If the second index is not given, it is considered as the length of the string.
4) If the first index is greater than the second index, the result will be an empty string.
5) If the first index is greater than the length of the string, the result will be an empty string.
6) If the second index is greater than the length of the string, it is considered as the length of the string.
'''


# Basic Operations on Strings ->
'''
1) Concatenation -> The + operator is used to concatenate two strings. For example, "Hello" + "World" will give "HelloWorld".

2) Repetition -> The * operator is used to repeat a string. For example, "Hello" * 3 will give "HelloHelloHello".

3) Slicing -> The [] operator is used to slice a string. For example, "Hello"[1:3] will give "el".

4) Length -> The len() function is used to find the length of a string. For example, len("Hello") will give 5.

5) Membership -> The in operator is used to check if a character or a substring is present in a string. For example, 'H' in "Hello" will give True.

6) Iteration -> The for loop is used to iterate through a string. For example, for i in "Hello": print(i) will give H e l l o.

7) Comparison -> The comparison operators are used to compare two strings. For example, "Hello" == "Hello" will give True.

8) Indexing -> The [] operator is used to access a character in a string. For example, "Hello"[1] will give "e".

9) Formatting -> The % operator is used to format a string. For example, "Hello %s" % "World" will give "Hello World".

10) Escape Sequence -> The \ character is used to escape special characters. For example, "Hello\nWorld" will give "Hello" on the first line and "World" on the second line.

11) Raw String -> The r character is used to create a raw string. For example, r"Hello\nWorld" will give "Hello\nWorld".

12) String Methods -> There are many built-in methods in Python that can be used to manipulate strings. For example, "Hello".upper() will give "HELLO".

13) String Formatting -> The format() method is used to format a string. For example, "Hello {}".format("World") will give "Hello World".

14) String Interpolation -> The f-string is used to format a string. For example, f"Hello {'World'}" will give "Hello World".

15) String Functions -> There are many built-in functions in Python that can be used to manipulate strings. For example, len("Hello") will give 5.

16) String Operations -> There are many operations that can be performed on strings. For example, "Hello" + "World" will give "HelloWorld".

17) String Constants -> There are many constants that are used in strings. For example, string.ascii_lowercase will give 'abcdefghijklmnopqrstuvwxyz'.

18) String Formatting -> There are many ways to format a string. For example, "Hello {}".format("World") will give "Hello World".
'''