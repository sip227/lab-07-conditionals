num1 = input("Gimme a number. ")
num2 = input("Gimme another number. ")
operation = input("Decide an operation. ")
if operation == "mul" or operation == "multiply": 
    print(int(num1) * int(num2))
elif operation == "div" or operation == "divide":
    print(int(num1) / int(num2))
elif operation == "mod" or operation == "modulo":
    print(int(num1) % int(num2))  
else:
    print("***invalid operation***")
            
