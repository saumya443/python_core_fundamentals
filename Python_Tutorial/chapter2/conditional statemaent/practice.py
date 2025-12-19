# n = int(input("enter a number : "))
# for i in range (1,11):
#    print(f"the table of the numbr is {n} * {i} = {n*i}")
   
# l = ["harry","saumya", "rahul" ]
# for i in l:
#     if (i.startswith("s")):
#         print("hello",i)
    
    
# n = int(input("enter the number: "))
# for i in range(2,n):
#     if(n%i)==0 :
#         print("number is not primre")
#         break
    
#     else:
#         print("number is  prime")
#         break
        
        
# n = int(input("enter the number to sum: "))
# i= 1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
    
# print(sum)            


# n = int(input("enter the number to factoril: "))
# i= n
# product=1
    
# print(product)            
# i= n
# product=1
# while(i>=1):
#     product *= i
#     i-=1
    
# print(product)  

n = int(input("enter the number to factoril: "))
product = 1
for i in range(1,n+1):
    product*=i
print(product)    