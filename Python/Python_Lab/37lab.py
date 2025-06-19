def add(a,b):
    result=a+b
    return result

def subtract(a,b):
    result=a-b
    return result

def multiply(a,b):
    result=a*b
    return result

def divide(a,b):
    if b != 0:
        result=a/b
    else:
        result="cannot divide by zero"
    return result
num1=10
num2=5

print("Addition",add(num1,num2))
print("subtraction:",subtract(num1,num2))
print("multiplication :",multiply(num1,num2))
print("division ")