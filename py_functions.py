# def <funcname>():
#     <actual code>


# def get_input_and_add():
    
#     a = input("Enter first number:")
#     b = input("Enter the second number:")
    
#     c = int(a) + int(b)
    
#     print("The addition is:",c)


# print("First time calling...")
# get_input_and_add()

# print("Second time calling...")
# get_input_and_add()

# print("Third time calling...")
# get_input_and_add()

# Function arguments

# def addition(a=20,b=25):
    
#     c = a+b
#     return c
    
# # firstnumber = 10
# # # secondnumber = 20
# # thirdnumber = 30

# # print("Calling addition function")
# # addition(firstnumber, thirdnumber)

# # addition("santosh","mani")
# # addition("santosh",10)

# # addition()

# # result = addition(10,20)
# # print(result)


# # res = addition(10)
# # print(res)


# # print(addition(10.2))
# name = "santosh"

# def find_sum_of_number(*given_nums):
#     print(given_nums)
#     print(type(given_nums))
#     global name
#     name = "deepti"
#     print(name)
    
#     res = 0
    
#     for nums in given_nums:
#         res = res + nums
    
#     print("The sum is :", sum)

# name = "mani"
# find_sum_of_number(1)
# # print(res)

# find_sum_of_number(1,5)

# find_sum_of_number(14,5,6,7,8,3)

# find_sum_of_number(134,23,423,354,534,34,234,54)
# print(name)

# import utils.mycalc as m
from utils.mycalc import *
import datetime
import boto3

print(dir(boto3))
# print(datetime.date())

print(dir(datetime))

import math

print(dir(math))

# print(dir(mycalc))

result = add(5,6)
print(result)

print(PI)
