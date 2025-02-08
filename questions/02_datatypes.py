# question 1:What are the different data types in Python? Give examples of each

d1 = "this is string" #string
d2 = 12 #number
d3 = None #use as a placeholder 
d4 = [1,2,3,4] #list
d5 = {"name":"vishal","partner":"unknown"} #dictionary
d6 = range(1,5,1) #range
d7 = {1,2,3,5,2,2,3} #set
d8 = True #boolean
d9 = ("stuff","needs","to","get","done")

# question 2:Identify the data type of the following:

42
3.14
'Hello, world!'
True
[1, 2, 3]
{ "name": "Alice", "age": 25 }

# question 3:How do you convert a string '123' into an integer?
str1 = "123"
num1 = int(str1)

# question 4:Write a Python program to check if a given variable is of type float.
def checkTypeIsFloat(input):
    return type(input)==float

result = checkTypeIsFloat(3.4)
# print(result)

# question 4:Convert the list [1, 2, 3, 4] into a tuple and a set.

l1 = [1, 2, 3, 4]
liTup = tuple(l1)
liSet = set(l1)

# question 5:Write a Python script to calculate the length of a string provided by the user.

def cal_length_of_str(input):
    return len(input)

# print(cal_length_of_str("here we go"))

# question 6:Create a dictionary to store details of a student (name, age, grade). Retrieve the age from the dictionary.

stud1 = {
    "name":"lexy",
    "age":12,
    "grade":"A"
}

# print(stud1["age"])

# question 7:Write a program to check if a variable is mutable or immutable.

def checkMutability(input):
    return type(input) == tuple or type(input) == str

# print(checkMutability(("hey", "there")))

# question 8:Convert the integer 10 to binary, octal, and hexadecimal formats.

num = 10

binary = bin(10)
# print(f"binary format of {num} is {binary}")
octal = oct(10)
# print(f"octal format of {num} is {octal}")
hexadecimal = hex(10)
# print(f"hexadecimal format of {num} is {hexadecimal}")

# question 9:Write a Python program to swap two numbers using tuple unpacking.

a = 10
b = 12
a,b = b,a
# print(a,b) 