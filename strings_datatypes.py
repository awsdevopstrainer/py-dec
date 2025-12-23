# mystring = 'santosh'

# print(type(mystring))

# # for char in mystring:
# #     print(char)

# print(mystring[1:4])

# mysentence = "Welcome 'to' python class"

# print(mysentence)

# myparagraph = '''
# Welcome to 'santosh'  \''' the 'python' string class
# this class \''' tells you how to use strings
# thanks
# '''

# print(myparagraph)


# mystring[2] = "k"

# print(mystring)



str1 = "santosh"
str2 = "Mani"
str3 = "venkat"
str4 = "deepti"
str5 = "praveen"

allnames = str1 + ',' + str2 +',' +  str3 + ',' + str4 + ',' + str5

print(allnames)

if str1 == str2 :
    print("str1 and st2 Both names are same")
else:
    print("str1 and st2 Both are different")
    
# print(len(str1))

# print(dir(str1))

print(str1.upper())

print(str2.lower())

print(allnames.partition("Mani"))

newallnames = allnames.replace(",",":")
print(newallnames)

print(newallnames.find("p"))


newstr = "    this         "
# print(newstr.rstrip())

# print(dir(newstr))

newstr = newstr.strip()

print(len(newstr))
