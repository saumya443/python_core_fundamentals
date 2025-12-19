class programmer():
    company = "Microsoft"
    def __init__(self,name,salary,languange):
        self.name= name
        self.salary=salary
        self.language=languange
p = programmer("harry",2345000,"java")
print(p.name,p.salary,p.language,p.company)        