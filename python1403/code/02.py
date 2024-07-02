#data type
#int float str bool

#input output
# user_input=input("Enter your input: ")
# print(user_input)

#define varible
# number=10
# number_2=2.0
# useranme="mahdi ramezani"
# flag=True

#opertaion in varible
#+ - / *  ** -> int float
# + 
#operation on int
#opertaion on float

#operation on string  -> sum,format string,index of string
name="mahdi"
family="ramezani"
# full_name=name +" "+ family
# print(full_name)
# full_name=f"Hello {name} {family}"
# print(full_name)
# full_name="{} {} {}".format(name,family,number)
# print(full_name)
# print(len(name))
# print(name[1:3])
#operation on bollean

#Type conversion  (int -> float) , ( float -> int ) , (int -> str ) , (str -> int )
# number=10
# number_2=2.0
# useranme="mahdi ramezani"
# flag=True

# print(f"type {number} is {type(number)}")
# print(f"type {number_2} is {type(number_2)}")
# print(f"type {useranme} is {type(useranme)}")
# print(f"type {flag} is {type(flag)}")

# int_to_float=float(number)
# float_to_int=int(number_2)
# print(float_to_int)

# price=23000000
# print(f"type {price} is {type(price)}")

# price_to_str=str(price)
# print(f"type {price_to_str} is {type(price_to_str)}")

# price="230000"
# print(type(int(price)))



#Type Hint in Python
# number:int=20
# float_number:float=20.0
# username:str="developer@"
# flag:bool=True

# number_1:int=input("Enter number 1: ")
# number_2:int=input("Enter Number 2: ")

# if (number_1 > number_2):
#     print(f"satet 1: {number_1} > {number_2}")

# elif (number_2 > number_1):
#     print(f"satet 2: {number_2} > {number_1}")

# elif (number_1 == number_2):

#     print(f"{number_2} == {number_1}")

# else:
#     print("Error")

# userinput=input("Enter number: ")

# print(type(userinput))

number_1:int=int(input("Enter number 1: "))
number_2:int=int(input("Enter Number 2: "))
operator:str=input("Enter + - * ** : ")



if (operator =="+"):
    sum_number=number_1+number_2
    print(f"{number_1} + {number_2} = {sum_number}")

elif (operator == "-"):
    print(f"{number_2} - {number_1} = {number_2-number_1}")

elif (operator == "*"):
    print(f"{number_1} * {number_2} = {number_1 * number_2}")

elif (operator == "**"):

    print(f"{number_1} ** {number_2} = {number_1 ** number_2}")

else:
    print("Erorr")


# print(10 < 20)

if (True):
    print("True")

elif(False):
    print("False")



#data structure
#List
#Dictionary












