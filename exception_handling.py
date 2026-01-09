print("Santosh")

# a = int(input("Enter first number:"))
# b = int(input("Enter Second number:"))

# c = a/b
# print(c)


try:
    a = int(input("Enter first number:"))
    b = int(input("Enter Second number:"))

    c = a/b
    print(c)
except ValueError:
    print("Hey please input only the integers!!!")
    
except ZeroDivisionError:
    print("Hey you have entered 0 for b!!!")

finally:
    print("The try block is over")

#####################################3
print("The next logic starts here...")
for i in range(10):
    print(i)
# except:
#     print("Hey some issue in the logic")

# c = a / b

# print(dir(locals()['__builtins__']))
