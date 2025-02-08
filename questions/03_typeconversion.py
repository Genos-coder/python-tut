# Question 1:What is the difference between implicit and explicit type conversion?

# implicit type conversions
"""
In implicit type conversion python convert data from smaller and less precision to larger and more precision in order to avoid the loss of data
"""

a = 10
b = 4.5
c = a + b # here the a is get's converted into floating point number
# print(c)

#Explicit type conversions
"""
This is done by programmer using build in functions 
"""

num1 = int("101")
num2 = float(10)
# print(num1, num2)

# Question 2:Which function would you use to convert a string "123" to an integer?

num3 = int("123")

# Question 3:Explain what happens when you convert a floating-point number to an integer.

"""answer
When you convert floating point number to integer it loses data and precision
"""

num4 = 10.34
num5 = int(num4)
# print(num5)


# Question 4:Predict the output

x = 5.7
y = int(x)
# print(y)

# Question 5:What will be the output of the following code?

num_str = "25"
num = int(num_str)
# print(num + 10)

# Question 6:Identify the error in this code and fix it

price = "30.5"
# total = price + 20
# total = int(float((price)))+20 # <--answer
# print(total)

# Question 6:Convert a list of strings to a list of integers

str_list = ["1", "2", "3", "4"]
int_List = []

for i in range(len(str_list)):
    int_List.append(int(str_list[i]))

print(int_List)