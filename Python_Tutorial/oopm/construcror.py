class Employee():
    def __init__(self,language,salary,city):
        
        self.languange = language
        self.salary= salary
        self.city=city
        print("That is my detail")
        
        
        
        
        
harry = Employee("py",2300000,"mumbai")
print(harry.salary,harry.languange)