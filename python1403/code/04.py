#string and list method

# full_name:str="mahdiI"
# price:str="1234m4"
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.isdigit())
# print(price.isdigit())
# full_name:str="mahdi,ramezani-22"
# print(full_name.split(","))

# user_input:list[int]=[]
# user_input=list()

# for  i in range(3):

#     user_input.append(input("Enter a number: "))

# print(user_input)

# for i in range(10):  #

#     print(f"loop 1: {i}")  #0

#     for j in range(10):  #0 1 2 3 4 5 6 7 8 9 

#         print(f"loop 2: {j}")

# for i in range(1,10):   

#     for j in range(1,10):  

#         print(i*j,end=" ") 

#     print("\n")  




#List Comprehensions

# numbers:list[int]=[1,2,3,4,5,6,7,8,9,10]

# new_list=[my_num for my_num in numbers if my_num %2 ==0]

# print(new_list)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# new_list=[x for x in fruits if "a" in x]

# print(new_list)

#nested loop and if 
#enomrate in loop

# names:list[str]=["mahdi","ali","reza","mohammad"]

# for name in names:

#     print(name)


# for i in range(len(names)):

#     print(f"{i}-{names[i]}")


# for i,name in enumerate(names,1):

#     print(i,name)


# numbers=[10,20,30,40,20,100,67]

# sum:int=0

# for number in numbers:

#     sum+=number

# print(sum)

# print(sum(numbers))

# number:int=100


# if number == 100:

#     if number % 2 == 0:

#         if (number / 2 == 50):

#             print(50)

# if ((number == 100) and (number %2 ==1)):

#     print("number")


# if ( (number==100) or (number%2==1)):

#     print("number")


# my_info:dict[str:str]={

#     "name":"ali",
#     "age":"25",
#     "family":"ahmadi"
# }

# # for item in my_info.keys():

# #     print(item)


# for k,v in my_info.items():

#     print(f"{k}:{v}")


data=[

    {
        "title":"Python",
        "teacher":"Amirhossein Amiri",
        "price":"free",
        "video":[

            {
                "name":"install python",
                "time":20,
            },

            {
                "name":"data type in python",
                "time":10
            },

            {
                "name":"if condition in python",
                "time":60
            }
        ]
    },


        {
        "title":"C++",
        "teacher":"Ahmad hafari",
        "price":"free",
        "video":[

            {
                "name":"install C++",
                "time":45,
            },

            {
                "name":"data type in C++",
                "time":18
            },

            {
                "name":"if condition in C++",
                "time":4
            },
            {
                "name":"oop in c++",
                "time":56
            }


        ]
    },

    
        {
        "title":"Dart",
        "teacher":"Sasan safari",
        "price":"free",
        "video":[

            {
                "name":"install Dart",
                "time":34,
            },

            {
                "name":"data type in Dartr",
                "time":18
            },

            {
                "name":"if condition in dart+",
                "time":48
            },
            {
                "name":"oop in dart",
                "time":6
            }


        ]
    },


]

sum_time:int=0

for item in data:

    for video in item["video"]:

        for k,v in video.items():

            sum_time+=video["time"]


print(sum_time)



