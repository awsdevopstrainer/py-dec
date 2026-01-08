# # f = open("myfirstfile.txt","w")

# # # print(f.readline())

# # # print(dir(f))

# # mycontent = """asdfasdfasddfasdf
# # this is a file that am creating in python
# # jaskldfjklasjdfklajskldjfas
# # dfaskldfkladsjfkljasdf

# # """

# # f.write(mycontent)
# # # f.close()

# # # f = open("myfirstfile.txt","w")

# # newcontent = "this is new content"
# # f.write(newcontent)

# # f.close()

# # f = open("myfirstfile.txt","r")

# # print(f.read())

# # alllines = f.readlines()

# # for line in alllines:
# #     print(line)

# f = open("myfirstfile.txt","r+")

# print(f.read())

# print(f.tell())

# print("second read:")
# f.seek(0)
# print(f.readlines())

# # newcontent = """
# # this is newfirst line"""

# # f.write(newcontent)

# f.close()


with open("myfirstfile.txt","r+") as f:
    print(f.read())

f.read()
