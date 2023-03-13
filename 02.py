# for i in range(0,20,5): #start End 

#     print(i)

# numbers=[]


# for i in range(5):

#     num=int(input(f"Enter Number{i+1}: "))
#     numbers.append(num)


# print(numbers)


# result=0

# for number in numbers:

#     result=result+number

# print(result)

#Q2:


# data=[]

# student={}

# for i in range(2):

#     name=input("Enter Your name: ")
#     family=input("Enter Family: ")
#     age=input("Enter Age: ")
#     score=input("Enter Scoure: ")

#     student["name"]=name
#     student["family"]=family
#     student["age"]=age
#     student["score"]=score

#     data.append(student)

# print(data)


#Q3:

# for i in range(1,10,1): #1 2

    

#     for j in range(1,10,1): #1

#         print(f"{i}*{j}={i*j}",end=" ")    #1*1 1*2 1*3 1*4 1*5 1...*9
#                               #2*1 2*2 2*3 ....2*9

#     print("\n")

#Q4:

# databse={
#     "course":{
#         "python":{
#             "teacher":"ali",
#             "time":10,

#         },

#         "java":{
    
#                 "teacher":"reza",
#                 "time":10,
#         }
#     },
   
# }

# for k,v in databse.items():

#     for i,j in v.items():
        
#         for x,y in j.items():

#             print(y)

#Q5 List To Str

# my_list=["mahdi","reza","ali"]

# my_str=""

# for name in my_list:

#     my_str=my_str+" "+name


# print(my_str)

#Q6 Str To List:

# my_str="mahdi"
# my_list=[]

# for char in my_str:

#     my_list.append(char)

# print(my_list)


my_str="mahdi,ramazani,age:20,city:bnd"

name_family=my_str.split(",")

print(name_family)


