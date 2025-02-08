# Question 1:What is the difference between local and global variables in Python?

"""Answer
The visibility and accessibility of variable is depend on where it got defined inside the if else, loop, class body, function block or outside it  
"""
# global scope

var1 = 10  # This is a global scope variable
if(True):
    # print(var1)
    pass

#local scope variable
if(True):
    var1 = 12 # local scope variable get's priority over global scope
    # print(var1)

#Question 2:What will happen if a local variable has the same name as a global variable?

"""Answer:
then the block will choose the local variable over the global
"""

# Question 3:Explain the global keyword in Python. When would you use it?

prop = "bat";

def changeProp():
    prop = "ball"  #even though we change the prop value it will still print the bat because it is a local scope 
    
changeProp()
# print(prop)


def changeProp2():
    global prop  
    prop = "ball" 
changeProp2()
# print(prop)

# So in order to change the global scope variable inside the block we need to use global keyword

# Question 4:Predict the output
x = 10
def my_function():
    x = 20
    print(x)
# my_function()
# print(x)

# Question 5:What will be the output of the following code?

count = 5
def increment():
    global count
    count += 1
increment()
# print(count)

# Question 6:Identify the error in the following code:


def calculate():
    total += 10 #unbound reference error
    print(total)

total = 0
# calculate()

# Question 7:Modify this code to use a global variable correctly

def update_balance(amount):
    balance = balance + amount

balance = 100
# update_balance(50)
# print(balance)

