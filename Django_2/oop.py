# class Car:


#     def __init__(self,name,model,max_speed=0):


#         self.name=name
#         self.model=model
#         self.max_speed=max_speed
#         self.is_on=False
#         self.is_off=True

#     def get_information(self):

#         print(self.name,self.model)

#     def start(self):

#         if self.is_on:

#             print("Erorr Car is On...")

#         else:

#             self.is_on=True

#             self.is_off=False

#             print("Car is On")

#     def Off(self):


#         if self.is_off:

#             print("Erorr Car is Off")

#         else:

#             self.is_on=False
#             self.is_off=True
#             print("Car is Off")


# car_1=Car("Pride","1399")

# # car_1.get_information()

# car_2=Car("Pars","2020",200)

# # car_2.get_information()

# car_1.start()
# car_1.Off()
# car_1.Off()


class User:


    def __init__(self,name,family):

        self.name=name
        self.family=family

    def get_information(self):

        print(self.name,self.family)


class Teacher(User):

    def __init__(self, name, family,age):
        User.__init__(self,name, family)
        self.age=age

    def get_information(self):
        print(self.age)
        return super().get_information()
        





# user_1=User("mahdi","ramezani")

# user_1.get_information()

t_1=Teacher("reza","ahmadi",22)
t_1.get_information()