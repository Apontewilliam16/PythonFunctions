# A function is defined using the def keyword
def my_functions():
    print("This is a basic funtion")

#To call a function, use the function name followed by parenthesis
my_functions()

# A variable could be passed on in a function  so later on it could be 
# used for specific task that may become repetative
def variable_function(fname):
    print(fname + " Aponte")

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

NumberOfArguments("William ","Aponte")

#If you try to call the function with 1 or 3 arguments
# you will get an error:

# NumberOfArguments("William")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, 
# and can access the items accordingly:

def ArbitraryArguments(*kids):
    print("The youngest child is " + kids[2]) #slice indexing 

ArbitraryArguments("Douglas","Tom","Mark")

#Keyword Arguments 
#Order does not matter 
def Keyword_Arguments (child3,child2,child1):
    print("The youngest child is " + child3)

Keyword_Arguments(child1= "Mike",child2="Josh",child3="Nick")

# Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

def AKA(**kid):
    print("His last name is "+ kid["lname"])

#argument could be set when calling upom the function 
AKA(fname = "Tobias", lname = "Santos")

#Default Parameter Value 
# The following example shows how to use a default parameter value 
# if we call the function without argument,it uses the default value:

def Default_Parameter_Value(country = "Norway"):
    print ("I am from "+ country)

Default_Parameter_Value("Sweden")
Default_Parameter_Value("Brazil")
Default_Parameter_Value("India")
Default_Parameter_Value()

#Passing a list as Arguments 
# You can send data types of arguments to a function (string,numbers,list,dictionary etc),
# and it will be treated as the same data types inside the function.
# if you send a list as an argument, it will still be a list when it reaches the function: 

def Passing_A_List(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]

Passing_A_List(fruits)

#Return Values 
# To let a function return a value, uses the return statment: 

def return_function(x):
    return 5*x 

print(return_function(3))
print(return_function(4))
print(return_function(5))

# The pass Statement 
# function definitions cannot be empty,but if you for some reason have a function 
# definition eith no content, put in the pass statement to avoid an error

def pass_statement():
    pass 

# Recursion = Function that call itself 
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
