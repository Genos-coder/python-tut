arr1 = [1, 2, 3, 4]
# print(arr1)
# print(arr1[::-1])

arr1.append(5)
arr1.insert(3,100)
arr1.extend([6,7,8,9])
# print(arr1)
arr2 = [10, 11]
# print(arr1+arr2)

arr3 = [1,2,3,4,5]
arr3.pop()
arr3.remove(2)
del arr3[0]
arr3.clear()
# print(arr3)

arr4 = [1,2,3,4]
arr4[2:3] = [10]
print(arr4)

# list comprehension

arr5 = [23,11,22,1111,32,211,34,44,2,3,4,123,6]

greaterThan_20 = [item for item in arr5 if item >20]
print(greaterThan_20)

arr6 = [1,2,3,4]
print(arr6.index(2))
print(arr6.count(2))
print(arr6.copy())
arr7 = [23,33,2,1,3]
arr7.sort()
arr7.sort(reverse=True)

print(arr7)
arr8  =["jake", "marry", "wanda"]

arr8.reverse()
print(arr8)




