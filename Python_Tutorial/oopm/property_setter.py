class Employee:
    @property
    def name(self):
        return f"Happy Birthday"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname =value.split(" ")[1]
        return f"{self.fname} {self.lname}"
e =Employee()
str= input("Enter your name : ")
e.name = str
print(e.fname,e.lname,e.name) 
# The class should have two attributes: marks1 and marks2.

# Define a property called total that returns the sum of marks1 and marks2.

# Define a setter for total that, when given a new total value, distributes it equally between marks1 and marks2.

# class student:
#     marks1 =0
#     marks2 =0
#     @property
#     def total(self):
#         return f"{self.marks1} + {self.marks2} = {self.marks1+self.marks2}"
#     @total.setter
#     def total(self,value):
#         self.marks1 = value //2
#         self.marks2 = value-self.marks1
# s= student()
# newtotal = int(input(f"Enter the total number : "))

# s.total=newtotal
# print(s.total, s.marks1, s.marks2)
# print("Hii everyone this saumya yadav your new mentor kaisse hai aap log , . ...<,K>