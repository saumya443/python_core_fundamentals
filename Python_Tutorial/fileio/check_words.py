with open("file.txt","r") as f:
    d = f.read()
    # if ("twinkle" in d):
    #     print("twinkle is present")
    # else:
    #     print("twinkle is not present")
     
l =["Saumya","Rahul","Shyam"]    
for i in l:
      d=d.replace(i,"#"*len(i))
with open ("file.txt","w") as f:
  f.write(d)
                