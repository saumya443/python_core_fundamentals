#  greatese among three number
def fun(a,b,c):
    if(a>=b and a>=c):
        print("a is greater")
              
    elif(b>=a and b>=c):
        print("b is greater")
    else:
        print("c is greatest")
        
fun(4,5,6)       

# pattern
def fun(n):
    if n==0:
        return
    print("*"*n)
    fun(n-1) 
    
fun(10)   
    
# listklp

def rmv(l, word):
   n =[]
   for item in l:
       n.append(item.strip(word))
   print(n)   
l = ["han","rohan","an"]    
rmv(l,"an")
        
