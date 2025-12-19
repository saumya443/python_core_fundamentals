# with open("fileio/filein","r") as f:
#     content = f.read()
#     print(content)
    

# lineno = 1 
# for line in f:
#     if("Saumya" in line):
#         print(f"Saumya present at lineno: {lineno}")
#         break
#     lineno+=1
# else:
#          print("Saumya is not present")
data =True
lineno =1   
with open("fileio/filein","r") as f:
    while data:
        data = f.readline()
        if ("Saumya" in data):
            print(f"Found saumya at {lineno}")
            break
        lineno+= 1
        
            
            
  

      

    