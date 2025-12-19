try:
    x = int(input("enter no."))
    ans = 10/x
    
except ZeroDivisionError:
    print(f"divide by zero is not allowed")
    
except ValueError:
    print("invalid input")
    
else:
    print(f"ans = {ans}")
    
finally:
    print("End the program")                    