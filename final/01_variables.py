name  = "abhishek"
age = 10
passed = True

# Variable name should be alphanumeric and should not start with number and $, non-alphanumeric stuff
# local scope variables

def sumTheNums(a, b):
    print(a+b)

sumTheNums(1, 2)
# print(result)

# cases to write the variable name

firstName = "ganesh" #camel case
LastName = "kale" #pascal case
access_token = "ASF232FF23" #snake_case

icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")
    print(icecream + " is a global variable value.")
    print(fruit + " is a local variable value.")

foods()


# Global variable
country = "india"
def checkgloble():
    state ="delhi"
    print(state ,country)


checkgloble()

