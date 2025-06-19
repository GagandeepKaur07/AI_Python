'''# write a python code to add 2 and 3 using the print() ;
print(2+3)

#insert a tab space between the output "hello" and "World" using the print() function
print("hello\tWorld")

#Create three Python vaiable 

a=10
b=20.5
c=4+3j
print(type(a))
print(type(b))
print(type(c))

#Assign you name in a variable and display it using print function 
Name= "Gagandee_Kaur_Rajpal"
print(Name)

#Demostrate the use of floor and exponentiatial

a=3
b=5

print(f"{a} // {b}= {a//b}")
print(f"{a} ** {b}= {a**b}")

#1. Write a Python program that:
#b. Performs an implicit conversion by adding an integer and a float.
#c. Then, performs an explicit conversion by converting the result into a string and concatenating it with another string.
int1=5
flo1=5.5
result=int1+flo1
print(int1+flo1)
print(type(result))
print(type(float(int1)))

#2. Write a Python program to display the following output using string literals and print formatting:
Name = "Alice"
Age = 25
Location = "New york"
print("Name is: {} \t Age is: {} \t Location is : {}".format(Name,Age,Location))

#Write Python code to calculate the square root of 8.4 (use **0.5), explicitly convert it to an integer, and display both the exact and rounded results
val=8.4
root=0.5
result=val**root
print(result)
print(type(int(result)))
print(type(result))

#Write Python code to assign a value x = 10 using a chained assignment (i.e., a = b = x) and calculate the product of a and b with an arithmetic operator.
x=10
a=b=x
pro=a*b
print(pro)

#Write Python code to calculate and print the result of this formula in a single line of code:
print((20+5*3)**2-(10/2))'''

#Write Python code to print the following text without using \n explicitly
print('''Hello World
Welcome to python
programming''')



#Assign three variables:
a=15
b=7
c=3
d=a**b/c+a%c
print(d)
