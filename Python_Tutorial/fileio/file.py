# read
# d = open("file.txt")
# content =d.read() # d.readlines(),d.readline()

# print(content)
# d.close()

# # write
# # sr = "Ram aayenge to angana saajungi"
# f = open("fle.txt" ,"w")
# f.write("I am Saumya")
# f.close()

# while read line
# d = open("file.txt")
# line = d.readline()
# while(line!=""):
#     print(line)
#     line=d.readline()
with open("fileio/filein","r") as d:
    content = d.read()
    # contentnew=content.replace("Radha","Saumya")
with open("fileio/filein","w") as d:
    d.write(content.replace("Saumya","Radha"))