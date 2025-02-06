str1 = "This is just started"

# print(str1 +" "+ "but wll end soon")
# print("Here \"Mermaid\" is not that tasty fish")

# mutiline string
str2 = """
First stipulation is you have to code
Second stipulation is you have to code
Third stipulation is you have to code
"""

str3 = '''
First task is focus on one thing
Second task is focus on one thing
Third task is focus on one thing
'''

# print("hi" in "hi there")
# print(str2)
# print(str3)


# operations on string

fruit = "Mango"
# print(len(fruit))

str4= "This string does the work"
# print(str4[0:4])
# print(str4[1:2])
# print(str4[:2])
# print(str4[1:])
# print(str4[1:-1])
# print(str4[1:-1+1])

for i in str4:
    # print(i)
    pass

# string methods

str5= "This is a testing string"

# print(str5.upper());
# print(str5.lower());
# print(str5.title());
# print(str5.capitalize());

str6 = "   test sting six  "
# print(str6.strip())

str7 = "home!!!"
# print(str7.rstrip("!"))

# print(str5.replace("is","is not",1))

str8 = "this thing ain't going anywhere"

# print(str8.split(" "))

# print(str8.islower())
# print(str8.isupper())
# print(str8.isalnum())

# print(str8.startswith("this"))
# print(str8.endswith("e"))

# print(" ".join(["why", "this", "kolaveri", "d"]))
str9 = "hEllo"
# print(str9.center(len(str8)+10,"*"))
# print(str9.rjust(10));
# print(str9.ljust(10,"!"));
# print(str9.count("l"))

# print(str9.index("l"))
# print(str9.find("l"))
# print(str9.find("f"))
# print(str9.index("f"))

# print(str9.swapcase())

# formatting in string

name = "ganesh"
age = 22
statement = "the name is {} and age is {}"
print(statement.format(name, age))

# using index to make string in order wise

sport = "cricket"
player = "kohli"
retired = "not"

statement2 = "does {2} who plays {1} is still {0} retired?"
print(statement2.format(retired,  sport,player))

# using f strings
print(f"player is {player} and sport is {sport}") 