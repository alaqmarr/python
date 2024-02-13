# In Python, we do not use {} curly brackets to define a block of code. Instead, we use indentation. The number of spaces is up to you as a programmer, but it has to be at least one. The only rule is that the number of spaces must be the same in the same block of code, otherwise, Python will give an error. The standard is to use four spaces.

# In Visual Studio Code, you can use the Tab key to indent the code. The Tab key will automatically insert four spaces. You can also use the Shift + Tab key to unindent the code.

# The deafult indentation in Visual Studio Code is 4 spaces. You can change it by clicking on the gear icon in the bottom right corner of the window and then clicking on the "Settings" option. In the search bar, type "tab size" and change the value to 4. You can also change the value of "detect indentation" to "true" to automatically detect the indentation of the file.

# We used "function" keyword to define a function in C language. In Python, we use "def" keyword to define a function.

def greet_user():
    name = input("Please tell us your Good Name: ")
    if(name == "" or name == " "):
        print("You did not enter your name. Please enter your name.")
        greet_user()
    elif (name):
        print("Hello "+name+"!\nWelcome to the world of Python Programming Language!\n")
        print("We are glad to have you here.\n")
        print("We hope you will have a great time learning Python.\n")
        mood = input("How are you feeling today? ")


# We have defined a function called "greet_user" in the above example. The function takes no arguments. The function takes the input from the user and stores it in the variable "name". The function then checks if the user has entered the name or not. If the user has not entered the name, the function will ask the user to enter the name again. If the user has entered the name, the function will display a welcome message and ask the user how they are feeling today.
# Now let's see how to call the function.

# In C language, we used to call the function by writing the name of the function followed by the parenthesis. In Python, we use the same technique to call the function.
        
greet_user()

