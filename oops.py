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


class Cars:
    # attributes
    # gears = 0
    # name = ""
    
    # constructor 
    def __init__(self, object_name="default", object_gears=0):
        
        self.name = object_name
        self.gears = object_gears
        if self.gears >= 5:
            self.power_rpm = 1000
        elif self.gears >=4 :
            self.power_rpm = 600
        else:
            self.power_rpm = 300
        print("The object is created with the name of "+object_name+" and with the gear of", object_gears, "and the power rpm is", self.power_rpm)
        
    # behaviours
    def get_info(self):
        print("The car name is:",self.name)
        print("The car has following gears:",self.gears)
        print("The power is ",self.power_rpm)

car1 = Cars("benz",5)
# print(car1.object_name)
# car1.get_info()

car2 = Cars("mercedes",6)
car2.get_info()
# car2.get_info()

car3 = Cars("kia",4)
# car3.get_info()

car4 = Cars("ford")
