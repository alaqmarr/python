# PLEASE READ THE PROBLEMS AND TRY TO SOLVE THEM, THEN RUN THE CODE TO CHECK YOUR ANSWERS.

# Problem 1 ->
'''
Q] Consider the following code snippet : not TRUE and FALSE or TRUE
Which of the following is the output of the above code snippet?
a) True
b) False
c) None
d) Error

SYNTAX: expression = not TRUE and FALSE or TRUE
        print(expression)
'''

# Problem 2 ->
'''
Q] Consider the following code snippet : 5 ** 2
Which of the following is the output of the above code snippet?
a) 25
b) 10
c) 7
d) 0

SYNTAX: expression = 5 ** 2
        print(expression)
'''

# Problem 3 ->
'''
Q] Consider the following code snippet : 10 + 20 * 30
Which of the following is the output of the above code snippet?
a) 600
b) 900
c) 300
d) 200

SYNTAX: expression = 10 + 20 * 30
        print(expression)
''' 

# Problem 4 ->
'''
Q] Consider the following code snippet : 10 + 20 * 30 / 40
Which of the following is the output of the above code snippet?
a) 30.0
b) 30
c) 30.5
d) 31

SYNTAX: expression = 10 + 20 * 30 / 40
        print(expression)
'''

# Problem 5 ->
'''
Q] Consider the following code snippet : 10 + 20 * 30 / 40 - 50
Which of the following is the output of the above code snippet?
a) -20.0
b) -20
c) -19.5
d) -21

SYNTAX: expression = 10 + 20 * 30 / 40 - 50
        print(expression)
'''

# Problem 6 ->
'''
Q] Consider the following code snippet : 10 + 20 * 30 / 40 - 50 * 2
Which of the following is the output of the above code snippet?
a) -40.0
b) -40
c) -39.5
d) -41

SYNTAX: expression = 10 + 20 * 30 / 40 - 50 * 2
        print(expression)
'''

# Problem 7 ->
'''
Q] Consider the following code snippet : 10 + 20 * 30 / 40 - 50 * 2 ** 3
Which of the following is the output of the above code snippet?
a) -60.0
b) -60
c) -59.5
d) -61

SYNTAX: expression = 10 + 20 * 30 / 40 - 50 * 2 ** 3
        print(expression)
'''


# Problem 8 ->
'''
Q] Create a program that takes a color as input and prints what to be done for that color on a traffic signal.
Below is the color and their respective meanings:
Red -> Stop
Yellow -> Wait
Green -> Go

SYNTAX: color = input("Enter a color: ")
        if(color == "Red"):
            print("Stop")
        elif(color == "Yellow"):
            print("Wait")
        elif(color == "Green"):
            print("Go")
        else:
            print("The light is broken.")
'''

# Problem 9 ->
'''
Q] Create a program that takes a number as input and prints if the number is positive, negative or zero.

SYNTAX: num = int(input("Enter a number: "))
        if(num > 0):
            print("The number is positive.")
        elif(num < 0):
            print("The number is negative.")
        else:
            print("The number is zero.")
'''

# Problem 10 ->
'''
Q] Create a program that takes a number as input and prints if the number is even or odd.

SYNTAX: num = int(input("Enter a number: "))
        if(num % 2 == 0):
            print("The number is even.")
        else:
            print("The number is odd.")
'''

# Problem 11 ->
'''
Q] Create a program that takes a number as input and prints if the number is a multiple of 5 or not.

SYNTAX: num = int(input("Enter a number: "))
        if(num % 5 == 0):
            print("The number is a multiple of 5.")
        else:
            print("The number is not a multiple of 5.")
'''

# Problem 12 ->
'''
Q] Create a program that taken marks as input and prints the grade according to the following criteria:
Marks -> Grade
90-100 -> A
80-89 -> B
70-79 -> C
60-69 -> D
50-59 -> E
<50 -> F

SYNTAX: marks = int(input("Enter your marks: "))
        if(marks >= 90 and marks <= 100):
            print("A")
        elif(marks >= 80 and marks <= 89):
            print("B")
        elif(marks >= 70 and marks <= 79):
            print("C")
        elif(marks >= 60 and marks <= 69):
            print("D")
        elif(marks >= 50 and marks <= 59):
            print("E")
        else:
            print("F")
'''

# Problem 13 ->
'''
Q] Create a program that takes integer between 1-5 and store as A. Then taka user's gender as input and store as G. Based on the value of A and the gender, print the fee for the user. The fee is calculated as follows:
A -> G -> Fee
1 -> M -> 300
1 -> F -> 250
2 -> M -> 450
2 -> F -> 400
3 -> M -> 550
3 -> F -> 500
4 -> M -> 700
4 -> F -> 650
5 -> M -> 900
5 -> F -> 850

SYNTAX: A = int(input("Enter a number between 1-5: "))
        G = input("Enter your gender: ")
        if(A == 1 and G == "M"):
            print("300")
        elif(A == 1 and G == "F"):
            print("250")
        elif(A == 2 and G == "M"):
            print("450")
        elif(A == 2 and G == "F"):
            print("400")
        elif(A == 3 and G == "M"):
            print("550")
        elif(A == 3 and G == "F"):
            print("500")
        elif(A == 4 and G == "M"):
            print("700")
        elif(A == 4 and G == "F"):
            print("650")
        elif(A == 5 and G == "M"):
            print("900")
        elif(A == 5 and G == "F"):
            print("850")
        else:
            print("Invalid input.")
'''

# Problem 14 ->
'''
Q] Write a program to take one side of a square as input and print the area of the square.

SYNTAX: side = int(input("Enter the side of the square: "))
        area = side * side
        print("The area of the square is: ", area)
'''

# Problem 15 ->
'''
Q] Write a program to take the radius of a circle as input and print the area of the circle.

SYNTAX: radius = int(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print("The area of the circle is: ", area)
'''

# Problem 16 ->
'''
Q] Write a program to take the length and breadth of a rectangle as input and print the area of the rectangle.

SYNTAX: length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        area = length * breadth
        print("The area of the rectangle is: ", area)
'''

# Problem 17 ->
'''
Q] Write a program to take the base and height of a triangle as input and print the area of the triangle.

SYNTAX: base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("The area of the triangle is: ", area)
'''

# Problem 18 ->
'''
Q] Write a program to take the side of a cube as input and print the volume of the cube.

SYNTAX: side = int(input("Enter the side of the cube: "))
        volume = side * side * side
        print("The volume of the cube is: ", volume)
'''

# Problem 19 ->
'''
Q] Write a program to take the radius of a sphere as input and print the volume of the sphere.

SYNTAX: radius = int(input("Enter the radius of the sphere: "))
        volume = (4/3) * 3.14 * radius * radius * radius
        print("The volume of the sphere is: ", volume)
'''

# Problem 20 ->
'''
Q] Write a program to take the length, breadth and height of a cuboid as input and print the volume of the cuboid.

SYNTAX: length = int(input("Enter the length of the cuboid: "))
        breadth = int(input("Enter the breadth of the cuboid: "))
        height = int(input("Enter the height of the cuboid: "))
        volume = length * breadth * height
        print("The volume of the cuboid is: ", volume)
'''

# Problem 21 ->
'''
Q] Write a program to input 2 float numbers and print their average.

SYNTAX: num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        avg = (num1 + num2) / 2
        print("The average of the numbers is: ", avg)
'''

# Problem 22 ->
'''
Q] Write a program to input 3 numbers and print their average.

SYNTAX: num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        avg = (num1 + num2 + num3) / 3
        print("The average of the numbers is: ", avg)
'''

# Problem 23 ->
'''
Q] Write a program to input 3 numbers and print the largest number.

SYNTAX: num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        if(num1 > num2 and num1 > num3):
            print("The largest number is: ", num1)
        elif(num2 > num3):
            print("The largest number is: ", num2)
        else:
            print("The largest number is: ", num3)
'''

# Problem 24 ->
'''
Q] Write a program to input 3 numbers and print the smallest number.

SYNTAX: num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        if(num1 < num2 and num1 < num3):
            print("The smallest number is: ", num1)
        elif(num2 < num3):
            print("The smallest number is: ", num2)
        else:
            print("The smallest number is: ", num3)
'''

# Problem 25 ->
'''
Q] Write a program to input 3 numbers and print the numbers in ascending order.

SYNTAX: num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        if(num1 < num2 and num1 < num3):
            if(num2 < num3):
                print("The numbers in ascending order are: ", num1, num2, num3)
            else:
                print("The numbers in ascending order are: ", num1, num3, num2)
        elif(num2 < num3):
            if(num1 < num3):
                print("The numbers in ascending order are: ", num2, num1, num3)
            else:
                print("The numbers in ascending order are: ", num2, num3, num1)
        else:
            if(num1 < num2):
                print("The numbers in ascending order are: ", num3, num1, num2)
            else:
                print("The numbers in ascending order are: ", num3, num2, num1)
'''

# Problem 26 ->
'''
Q] Write a Program to input user's name and print the length of the name.

SYNTAX: name = input("Enter your name: ")
        print("The length of your name is: ", len(name))
'''

# Problem 27 ->
'''
Q] Write a program to input a string and print the string in uppercase.

SYNTAX: string = input("Enter a string: ")
        print("The string in uppercase is: ", string.upper())
'''

# Problem 28 ->
'''
Q] Write a program to input a string and print the string in lowercase.

SYNTAX: string = input("Enter a string: ")
        print("The string in lowercase is: ", string.lower())
'''

# Problem 29 ->
'''
Q] Write a program to input a string and print the string in title case.

SYNTAX: string = input("Enter a string: ")
        print("The string in title case is: ", string.title())
'''

# Problem 30 ->
'''
Q] Write a program to input a string and print the string in reverse.

SYNTAX: string = input("Enter a string: ")
        print("The string in reverse is: ", string[::-1])
'''

# Problem 31 ->
'''
Q] Write a program to input a string and print the string in reverse without using the reverse function.

SYNTAX: string = input("Enter a string: ")
        rev = ""
        for i in range(len(string) - 1, -1, -1):
            rev += string[i]
        print("The string in reverse is: ", rev)
'''

# Problem 32 ->
'''
Q] Write a program to fine the occurence of a character in a string.

SYNTAX: string = input("Enter a string: ")
        char = input("Enter a character: ")
        print("The occurence of the character is: ", string.count(char))
'''

# Problem 33 ->
'''
Q] Write a program to replace a character in a string with another character.

SYNTAX: string = input("Enter a string: ")
        char1 = input("Enter a character to be replaced: ")
        char2 = input("Enter a character to replace with: ")
        print("The new string is: ", string.replace(char1, char2))
'''

# Problem 34 ->
'''
Q] Write a program to input a string and print the number of words in the string.

SYNTAX: string = input("Enter a string: ")
        print("The number of words in the string are: ", len(string.split()))
'''

# Problem 35 ->
'''
Q] Write a program to input a string and print the number of characters in the string.

SYNTAX: string = input("Enter a string: ")
        print("The number of characters in the string are: ", len(string))
'''

# Problem 36 ->
'''
Q] Ask user to enter their favourite movies and store them in a list. Then print the list.
    Seperate movies using comma.

SYNTAX: movies = input("Enter your favourite movies: ").split()
        print("Your favourite movies are: ", movies)
'''

# Problem 37 ->
'''
Q] Write a program to input a list of numbers and print the sum of the numbers.

SYNTAX: numbers = list(map(int, input("Enter a list of numbers: ").split()))
        print("The sum of the numbers is: ", sum(numbers))
'''


# Problem 38 ->
'''
Q] Write a program to count the number of students with a specific grade in a given list of grades.

SYNTAX: grades = ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F']
        grade = input("Enter a grade: ")
        print("The number of students with the grade are: ", grades.count(grade))
'''

# Problem 39 ->
'''
Q] Write a program to count the number of students with a specific grade in a given touple of grades.

SYNTAX: grades = ('A', 'B', 'C', 'A', 'B', 'A', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F')
        grade = input("Enter a grade: ")
        print("The number of students with the grade are: ", grades.count(grade))
'''

# Problem 40 ->
'''
Q] Store the below values in a list and sort the list in ascending order.
    10, 99, 45, 23, 78, 56, 89, 34, 67, 12

SYNTAX: numbers = [10, 99, 45, 23, 78, 56, 89, 34, 67, 12]
        numbers.sort()
        print("The sorted list is: ", numbers)
'''

# Problem 41 ->
'''
Q] Store the below values in a list and sort the list in descending order.
    'A', 'Z', 'B', 'Y', 'C', 'X', 'D', 'W', 'E', 'V'

SYNTAX: letters = ['A', 'Z', 'B', 'Y', 'C', 'X', 'D', 'W', 'E', 'V']
        letters.sort(reverse = True)
        print("The sorted list is: ", letters)
'''