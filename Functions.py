# A function is defined using the def keyword
def my_functions():
    print("This is a basic funtion")

#To call a function, use the function name followed by parenthesis
my_functions()

# A variable could be passed on in a function  so later on it could be 
# used for specific task that may become repetative
def variable_function(fname):
    print(fname + "Aponte")

variable_function("Giselle")
variable_function("Willam")

# The terms parameter and argument can be used for the same thing: information that are passed into a function.
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.


# A function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, 
# you have to call the function with 2 arguments, not more, and not less.
def NumberOfArguments(fname,lname):
    print(fname + "" + lname)

NumberOfArguments("William","Aponte")

#If you try to call the function with 1 or 3 arguments
# you will get an error:

# NumberOfArguments("William")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, 
# and can access the items accordingly:

def ArbitraryArguments(*kids):
    print("The youngest child is " + kids[0])

ArbitraryArguments("Douglas","Tom","Mark")

