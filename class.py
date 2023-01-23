# class Car:
#     name = "Premio"
#     color = "white"

#     def start():
#         print("Starting the engine")


# print("Name of the car:", Car.name)
# print("Color:", Car.color)

# Car.start()
# ---------------------
# class Car:
#     name = ""
#     color = ""

#     def start():
#         print("Starting the engine")


# Car.name = "Axio"
# Car.color = "Black"
# print("Name of the car:", Car.name)
# print("Color:", Car.color)

# Car.start()
# print(dir(Car))
# #---------------------

# class Car:
#     name = ""
#     color = ""

#     def start():
#         print("Starting the engine")

# # creating a Car object
# my_car = Car()
# my_car.name = "Allion"
# print(my_car.name)
# my_car.start()
# ----------------------

# #corrected code with self
# class Car:
#     name = ""
#     color = ""

#     def start(self):
#         print("Starting the engine")

# # creating a Car object
# my_car = Car()
# my_car.name = "Allion"
# print(my_car.name)
# my_car.start()

# -------------------

# class Car:
#     # name = ""
#     # color = ""

#     def __init__(self,name,color):
#         self.name=name
#         self.color = color

#     def start(self):
#         print("Starting the engine")

# my_car = Car("Corolla", "white")
# print(my_car.name)
# print(my_car.color)
# my_car.start()

# -----------------------------------------

# creating multiple objects

class Car:
    def __init__(self, n, c):  # this is a constructor
        self.name = n
        self.color = c

    def start(self):
        print("name: ", self.name)
        print("color: ", self.color)
        print("Starting the engine")
        print("----------------------------")


my_car1 = Car("Corolla", "White")
my_car1.start()
my_car2 = Car("Premio", "Black")
my_car2.start()
my_car3 = Car("Allion", "Blue")
my_car3.start()
