# class Cars:
#     # attributes
#     gears = 0
#     name = ""
    
#     # behaviours
#     def get_info(self):
#         print("The car name is:",self.name)
#         print("The car has following gears:",self.gears)
        

# car1 = Cars()

# # print(type(car1))
# # print(dir(car1))

# car1.name = "benz"
# car1.gears = "auto"

# # print("The car name is")
# # print(car1.name)

# car1.get_info()

# # print("The gears are")
# # print(car1.gears)

# car2 = Cars()
# car2.name = "tata"
# car2.gears = 4

# # print(car2.name)

# car2.get_info()


# class Cars:
#     # attributes
#     # gears = 0
#     # name = ""
    
#     # constructor 
#     def __init__(self, object_name="default", object_gears=0):
        
#         self.name = object_name
#         self.gears = object_gears
#         if self.gears >= 5:
#             self.power_rpm = 1000
#         elif self.gears >=4 :
#             self.power_rpm = 600
#         else:
#             self.power_rpm = 300
#         print("The object is created with the name of "+object_name+" and with the gear of", object_gears, "and the power rpm is", self.power_rpm)
        
#     # behaviours
#     def get_info(self):
#         print("The car name is:",self.name)
#         # print(f"the car name is {self.name}")
#         print("The car has following gears:",self.gears)
#         print("The power is ",self.power_rpm)




# car1 = Cars("benz",5)
# # print(car1.object_name)
# # car1.get_info()

# car2 = Cars("mercedes",6)
# car2.get_info()
# # car2.get_info()

# car3 = Cars("kia",4)
# # car3.get_info()

# car4 = Cars("ford")

# class Animal:
#     name = ""
    
#     def run(self):
#         print("Animals will run")
    
#     def eat(self):
#         print("Animals will eat")
        
# class LivingBeings:
#     def eat(self):
#         print("All living beings will eat")

# class Dog(LivingBeings, Animal):
#     breed = ""
    
#     def bark(self):
#         print("I can bark",self.name)
   
   
# puppy = Dog()

# puppy.eat()

     
# class Cat(Animal):
#     breed = ""
    
#     def sound(self):
#         print("I can make noise like meaw")

# class Tigor(Animal):
#     breed = ""
    
#     def roar(self):
#         print("I can roar")

# lab = Dog()

# lab.breed = "Labrador"
# lab.name = "MyPuppy"
# print(lab.name)
# lab.bark()
# lab.run()

# pug = Dog()



class Vehicle:
    # attributes
    # gears = 0
    # name = ""
    # tyres = 4
    
    
    # constructor 
    def __init__(self):
        self._tyres = 4
    
    def get_tyres(self):
        print("there are",self._tyres,"tyres")
        
    #     self.tyres = 4
    # def set_mode(self.)
    def get_ride(self):
        print("The vehicle is riding")

    # behaviours
    def get_info(self):
        print("The vehicle name is:",self.name)
        # print(f"the car name is {self.name}")

class Car(Vehicle):
    
    def __init__(self, carname, gears, mode):
        super().__init__()
        self.name = carname
        self.gears = gears
        self.__mode = mode
        
    def __speed(self):
        print("The car is riding in speed mode")
        
    def set_mode(self, mode):
        self.__mode = mode
        
    def get_info(self):
        super().get_info()
        print("the car name is ", self.name, self._tyres)
        
    def ride(self):
        self.__speed()
        print("car is riding in ",self.__mode,"mode")
        
car1 = Car("benz",5,"auto")
car1.get_info()
car1.get_tyres()
# print(car1._tyres)
# print(car1.name)
# car1.name = "newbenz"
# print(car1.name)

# car1.ride()
# # car1.__mode = "manual"
# car1.set_mode("manual")
# car1.ride()
# print(car1.tyres)
# # car1.__speed()


# print(4+4)

# print("a"+"b")

# a = "santhosh"
# b = [2,3,42,34,234,234]

# print(len(a))
# print(len(b))
