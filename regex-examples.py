import re

mytext = """this is gmail.com and you can call me anytime
also you can talk  one of the text file from Santosh,
I can be reached. at 9987767799 or +919988775544 and my email is 
santhosh_12345@email.in visual path Admin@visualpath.com
"""

# myresult = re.findall(r"\+?\d{10,12}",mytext)

# emails = re.findall("[A-Za-z0-9_]+@[a-z]+\.[a-z]+",mytext)
# print(emails)

pattern = re.compile("[A-Za-z0-9_]+@[a-z]+\.[a-z]+")

emails = pattern.findall(mytext)
print(emails)

# subsc = re.sub("[A-Za-z0-9_]+@[a-z]+\.[a-z]+","mynewid@abc.com",mytext)
# print(subsc)

# splitstring = re.split("\s", mytext)
# print(splitstring)


# print(dir(re))
# re.sub()

# print(myresult)
