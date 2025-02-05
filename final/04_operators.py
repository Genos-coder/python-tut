# Arithmatic operators

# print(12 + 10)
# print(12 - 10)
# print(12 / 10)
# print(12 * 10)
# print(2 ** 2)
# print(11 % 2)
# print(12 // 10) #divide the number and return floor value

# Assignment operator
a= 10
a +=10
a*=10
a /= 10
a -=10
a //=10
a **=10
a %= 10

# bitwise operator
# print(a)

b = 10
c = 12
# print(c & b)
# print(True & False)
# print(True | False)
# print(~True)
# print(True ^ False)

#comparison operator

# print( b < c)
# print( b > c)
# print( b != c)
# print("1" == 1)

d = 10
e = d
team1 = {"one":"faiz","two":"messi"}
team2 = team1
team3 = {"one":"faiz","two":"messi"}
print(team2 is team1)
print(team3 is team1)
print(d is e)

# Logical operators

# age = input("Enter your age:")
age = 20

if age >= 18 and age < 55:
    print("your are eligible to drive")
elif age < 18 or age >55:
    print("Your not eligible to drive")
else:
    print("The input you have typed is not compatible")

#  operator

print("one" in team2)
print("two" not in team2)

