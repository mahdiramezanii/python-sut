# print("hello world")

# my_list=["1","2"]

# my_list.append(2)


# def my_func():

#     print("Hello im fuunction")


# my_func()


# def my_func():


#     return "Hello World"


# print(my_func())

# def name_family(name,family):


#     print(name," ",family)

# name="mahdi"
# family="ramezani"
# name_family(name,family)



# def remove_item(my_list,item):


#     for i in my_list:

#         if i == item:

#             my_list.remove(i)

#     return my_list

# my_list=["m","a","a","b","d"]

# result=remove_item(my_list,"a")

# print(result)


# def sum_number(num1,num2):


#     result=num1+num2
    
#     return result


# number_1=10
# number_2=20

# print(sum_number(number_1,number_2,10))


# def sum_number(*args):


#     result=0

#     for number in args:

#         result+=number #result=result+number

#     return result    


# print(sum_number(1,2,3,4,10))

# from function import sum_number as s


# print(s(10,20,10,10,50))

# def myFun(x, y):
#     print("x: ", x)
#     print("y: ", y)
  
  
# Driver code (We call myFun() with only
# argument)
# myFun(10,10)


class User:


    def __init__(self,name,family):

        self.name=name
        self.family=family

    def get_information(self):

        print(self.name)
        print(self.family)
    

user_1=User("mahdi","ramezani")

user_1.get_information()


user_2=User("reza","ahmadi")

user_2.get_information()








    




