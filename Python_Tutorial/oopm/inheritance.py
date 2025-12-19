class dad():
    expression ="Angry"
    Voice = "strong"
    company = "samy"
    def fun(self):
      
        self.company="Ramy"
        print(f"I am the human being working in : {self.company}")
class baby(dad):
    def fun(self):
        print("my look is smart")
a =dad()
b=baby()
print(b.expression,b.Voice)  
a.fun()     
