# tup = (1, 5, 4, 9)
# print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])


# countries = ("India", "England", "Russia", "Spain", "Italy")
# temp = list(countries)
# temp.append("Bhutan")  #Add item
# temp.pop(2) #Remove item
# temp[3] = "Germany" #Change item
# countries = tuple(temp)
# print(countries)


# countries = ("India", "England", "Japan", "Bhutan")
# countries1 = ("Nepal", "China", "Spain")
# Total = countries + countries1
# print(Total)


# tuple1 = (1, 2, 7, 3, 6, 4, 3, 2, 3, 2, 3)
# es = tuple1.count(3) # [same elements count]
# res = tuple1.index(3) #position of digit
# print('Count of 3 in tuple1 is :', es)
# print("Position of digit is : ", res)


# Tuple Operations 

# # 1. Concatenation
# tuple1 = (5,4,3)
# tuple2 = (1,2)
# combine = tuple1+tuple2
# print("Concatenation of tuple : ", combine)

# # 2. Repetition 
# tuple3 = ("Hello ") * 4
# print(tuple3)

# 3. Checking for an Item 
# Use the in keyword to check if an item exists in a tuple. 
numbers = (10, 20, 30, 40) 
print(20 in numbers)  # Output: True 
