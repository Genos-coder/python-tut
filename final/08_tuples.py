tup1 = ("infinity war","marvel")
# can't alter the tuple
tupList = list(tup1)
tupList.pop(1)
newTup1 =tuple(tupList)

print(newTup1)

# unpacking the tuples

(movieName, studio ) = tup1
print(movieName, studio)

for i in tup1:
    # print(i)
    pass

# checking something present in tuple using membership operators


# if "marvel" in tup1:
#     print("The movie is created by marvel")
# else:
#     print("Movie is created by something else")