# DICTIONARY IN PYTHON

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

# example
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict)
# # This will print {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

me = {
    "name": "Al Aqmar",
    "age": 20,
    "phone": 9618443558,
    "college": "SVIT"
}
print(me)
# This will print {'name': 'Al Aqmar', 'age': 20, 'phone': 9618443558, 'college': 'SVIT'}

print(me["name"])
# This will print Al Aqmar

me["age"] = 21
# This will change the value of age from 20 to 21

# Like this we can access the values of the dictionary using the keys.

'''
PROPERTY OF DICTIONARY:
1-> Dictionaries are changeable, meaning that we can change, add, and remove items after the dictionary has been created.
2-> Dictionaries are unordered, meaning that the items have no defined order.
3-> Dictionaries are indexed, meaning that the items have a defined index.
4-> Dictionaries are written with curly brackets, and have keys and values.
5-> The keys in the dictionary must be unique.
6-> The values of a dictionary can be of any data type.
7-> The keys must be of an immutable data type such as strings, numbers, or tuples.
8-> The values of a dictionary can be of any data type.
'''

# EXAMPLE

students = {
    "Al Aqmar": {
        "name": "Al Aqmar",
        "age": 20,
        "phone": 9618443558,
        "college": "SVIT"
    },
    "Another Student": {
        "name": "Another Student",
        "age": 20,
        "phone": 1234567890,
        "college": "Another College"
    }
}

print(students)

name = input("Enter the name of the student: ")
print(students[name])
# This will print the details of the student whose name is entered by the user


# Create a dictionary with 15 students and their details and print the details of the student whose name is entered by the user.

students = {}
numberOfStudents = int(input("Enter the number of students: "))
for i in range(numberOfStudents):
    name = input("Enter the name of the student("+str(i+1)+"): ")
    age = int(input("Enter the age of the student("+str(i+1)+"): "))
    phone = int(input("Enter the phone number of the student("+str(i+1)+"): "))
    college = input("Enter the college of the student("+str(i+1)+"): ")
    students[name] = {
        "name": name,
        "age": age,
        "phone": phone,
        "college": college
    }

print(students)
name = input("Enter the name of the student: ")
print(students[name])
# This will print the details of the student whose name is entered by the user