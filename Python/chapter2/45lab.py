def divide_number():
    try:
        num1=float(input("enter the 1 number:"))
        num2=float(input("enter the 2 number:"))
        result=num1/num2
        print(result)
    except ZeroDivisionError:
        print("Error: cannot divide by zero:")
    except ValueError:
        print("Error : enter valid numeric number")
    finally:
        print("divide operation completed.")

divide_number()