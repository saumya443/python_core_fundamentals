with open("file.txt") as f:
    c = f.read()
    
with open("fle.txt") as d:
    c2 = d.read()
    
if (c==c2) :
    print("same")
else:
    print("not same")           