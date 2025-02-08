# Question 1:What will be the output?

a = 15
b = 4
# print(a // b) #floor division operator
# print(a % b)
# print(a ** b) # Exponentiation operator

# Question 2:Write a program to calculate the area of a circle given its radius. (Use the formula area = π * r²)

def find_area_of_circle(radius):
    return 3.14 * (radius**2)

# print(find_area_of_circle(4))


# Question 3:Predict the output:

x = 10
y = 20
# print(x > y)
# print(x <= y)
# print(x == 10)

# Question 4:What will be the output?

a = True
b = False
# print(a and b)
# print(a or b)
# print(not a)

# Question 5:Convert 5 and 3 to binary and calculate 5 & 3, 5 | 3, and 5 ^ 3.

binary_5 = bin(5)
binary_3 = bin(3)

# print(f"binary of 5 is {binary_5}")
# print(f"binary of 3 is {binary_3}")

r1 = 5|3
r2 = 5&3
r3 = 5^3
# print(f"bitwise or between 5, 3 is {r1}")
# print(f"bitwise and between 5, 3 is {r2}")
# print(f"bitwise XOR between 5, 3 is {r3}")

# Question 6:What does 5 << 2 and 10 >> 1 mean? Calculate their results.

# print(5<<2) # here binary representation of 5 is 0101 and it get's left shift  2 and this means 0101 -> 00010100 = 20
# print(10>>1) # here binary representation of 10 is 1100 and it get's left shift by 2 and this means 0101 -> 0011 = 5

# also we can use this formula
"""
digit << n = digit * 2**n
digit >> n = digit / 2**n
"""

# Question 7:Write a program that uses +=, -=, *=, and /= to modify a variable

def modify_value(value):
    value +=value
    value /=value
    value -=value
    value *=value
    return value

# print(modify_value(20))


# Question 8:What will be the output?

a = [1, 2, 3]
b = a
c = [1, 2, 3]
# print(a is b)
# print(a is c)
# print(2 in a)
# print(4 not in a)

"""
Question 9:Write a Python program that takes an integer input and:
Checks if it’s even or odd using the modulus operator.
Verifies if the number is between 10 and 50 using logical operators.
Uses a bitwise operator to multiply the number by 4.
"""
def ops_performer(input):
    if(input % 2 ==0):
        print("It is a even number")
    else:
        print("It is a odd number")
    if(input >10 and input <50):
        print("The number is greater than 10 and less that 50")
    input = input << 2
    print(input)

ops_performer(12)
