# Question 1:Which of the following values will be evaluated as False by the bool() function?

"Hello"
0
[]
-1
{}
None
# print(bool("hello"),bool(0),bool([]),bool(-1),bool({}),bool(None))

# Question 2:Predict the output:


# print(bool([]))
# print(bool(0))
# print(bool("Python"))
# print(bool(None))

# Question 3:Write a Python program that takes user input and checks if it's a falsy value.

def check_falsy(input):
    return bool(input)

# print(check_falsy(0))

# Question 4:Identify the falsy values in this list:

my_list = [0, 1, "", "Hello", [], [1, 2, 3], None, False]

for i in range(len(my_list)):
    # print(bool(my_list[i]))
    pass

# Question 5:Explain why the output of bool(0.0) is False but bool(0.00001) is True.
"""
Here the all forms of zero are 0, 0.0 ,00, 0j are all false
so 0.0 is false
but 0.00001 is too small value still it's not a zero 
"""
# print(bool(0.0))
# print(bool(0.00001))
"""
Question 6: Write a function that removes all falsy values from a list.

Input: [0, 1, "", None, [], "Python", False, 10]  
Output: [1, "Python", 10]
"""
def remove_falsy(input_list):
    new_list = []
    for i in range(len(input_list)):
        if(bool(input_list[i])):
            new_list.append(input_list[i])
    return new_list

# print(remove_falsy([0, 1, "", None, [], "Python", False, 10] ))