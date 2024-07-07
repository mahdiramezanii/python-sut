#list
# my_list=[1,"mahdi",2.9,True]

# print(my_list)
# print(type(my_list))

# my_list:list[int]=[1,2,3,4,5,6,7,8,9,"test"]
# # print(my_list[1:4])
# # print(my_list[1:4])
# # print(len(my_list)
# # print(my_list[len(my_list)-1])
# print(my_list[-1])


my_list = ["apple", "banana", "cherry"]

# my_list.append("reza")
# my_list.append(12)
# my_list.insert(1,"ali")

# my_list2:list[str]=["reza","ahmad","ali"]

# my_list.extend(my_list2)

# my_list.clear()

# print(my_list.index("banana"))

# print(my_list)

# numbers:list[int]=[2,3,120,45,67,89,90]

# numbers.sort()

# print(numbers)






#dictinary

# my_info={
#     "name":"reza",
#     "family":"ahmadi",
#     "age":22,
#     "city":"sirjan"
# }

# print(my_info["name"])
# print(my_info["age"])

# my_info["name"]="student"
# print(my_info.keys())
# print(my_info.values())
# print(my_info.items())

#while

# while (True):

#     print("Hwllo while")

# number:int=0

user_list:list[str]=[]

flag:bool=True

while (flag):

    user_input=input("Enter name(exit=0): ")

    if user_input =="0":

        flag=False

    else:    
        user_list.append(user_input)

print(user_list)



# while (number <= 10):

#     print(number)  #0 1 ..... 9

#     number=number+1 #1 2 3 4 5 6 7 8 9 10


#for

# users:list[str]=["ali","reza","mohammad"]

# for item in users:

#     print(item)

# [1,2,3,4,5,6,7,8,9]

# for number in range(1,10,2):
#     print(number)


# userinput:int=int(input("Enter number: "))

# for i in range(userinput+1):

#     print(i)

# user_list:list[str]=[]


# for i in range(5):

#     name=input(f"Enter name {i+1}: ")

#     user_list.append(name)


# print(user_list)



