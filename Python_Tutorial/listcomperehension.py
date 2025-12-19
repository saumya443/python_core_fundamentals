sq = []
for i in range(6):
    sq.append(i*i)
    
print(sq)
#2
sq = [i*i for i in range(6)]
print(sq)
    
 #3   
sq = [i*i for i in range (6) if (i%2)!=0]

#4
nums=[-2,-3,3,4,-1,7]
nums =[0 if val<0 else val for val in nums ]
print(nums)

#5
words =["hello", "python","sam"]
print(words[0].upper())
words = [val.upper() for val in words]
print(words)