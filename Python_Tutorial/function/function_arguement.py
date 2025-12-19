# def fun(name):
#     print(" good bye, ",name)
    
# fun    ("harry")
# fun("madhav")    

# recursion
def fun(n):
    if (n==1 or n==0):
        return 1
    return n+fun(n-1)

a =fun(4)
print(a)
                  