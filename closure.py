# functions can be assigned to a variable

# def greetings():
#     print("Hello guys")
    

# sayhello = greetings
# sayhello()

# function can be passed as a arguements
# def welcome(func):
#     func()

# def greetings():
#     print("Hello guys!!!")

# welcome(greetings)

# function can be returned from another function


# def outerfunc():
#     print("This is from outer function")
    
#     def innerfunc():
#         print("Hey I'm from inner function")
        
#     return innerfunc

# # print(outerfunc())
# calling = outerfunc()

# print("Now i will call the returned inner function")

# calling()


# def somefunc():
#     message = "my message"
    
#     return message

# somefunc()
# print(message)


# def outerfunc():
#     message = "Hey I'm Santhosh"
#     print("This is from outer function")
    
#     def innerfunc():
#         print("Hey I'm from inner function", message)
        
#     return innerfunc

# # print(outerfunc())
# calling = outerfunc()

# print("Now i will call the returned inner function")

# calling()

# calling()

# calling()


def counter():
    count = 0
    
    def increment_num():
        nonlocal count
        count += 1
        return count
    
    return increment_num

cnt = counter()

print(cnt())
print(cnt())

cnt = counter()
print(cnt())
print(cnt())
print(cnt())
print(cnt())
print(cnt())
