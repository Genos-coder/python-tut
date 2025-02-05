# numeric data
num1 = 12
num2 = 2.33
complexNum = 2 + 3j
# print(type(complexNum))
# print(type(num1))
# print(type(num2))

# Text data
st1 = "Hello there"

# Boolean
isTrue = True
isHealthy = False

# sequenced data

# 1.List

mixList = [1,2,True,[1,2,3],"hat"]

# print(mixList)

# 2.tuple

tuple1 = (1,2,3)
# print(tuple1)

tuple2  = (("ping","100"),("org","ff"))

# 3.range
r1 = range(1,10,2)
# print(list(r1))
for i in r1:
    i

# 4.dictionary

dict1 = {"name":"ted","last":"talks"}
print(dict1)

#5.Converting string to bytes
str1 = "This is a string"
arr1 = bytes(str1, 'utf-8')
# print(arr1)
arr2 = bytes(str1, 'utf-16')
# print(arr2)

# Creating bytes of given size
# bytestr = bytes(4)
# print(bytestr)

# 6.set

numSet = {1,2,33,4,1,1}
# print(numSet)


