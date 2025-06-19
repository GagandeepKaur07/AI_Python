import os 
def divide_number(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
def access_list(lst,index):
    try:
        return lst[index]
    except IndexError:
        return "Error: index is out of  range."
def get_dic_value(dct,key):
    try:
        return dct[key]
    except KeyError:
        return "Error : key not found in dictionary"
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "Error : invalid type for convertion."
    

# Task 2: Demonstration of different exceptions 
print("division example :")
print(divide_number(10,0))

print("list access example")
my_list=[1,2,3]
print(access_list(my_list,5))

print("dictionary example")
my_dict={'a':1,'b':2,'c':3}
print(get_dic_value(my_dict,'d'))

print("convertion")
print(convert_to_int('123abc'))
print(convert_to_int(123.45))
