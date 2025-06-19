n1=int(input("Enter the Starting number : "))
n2=int(input("Enter the endig number :"))
a,b=0,1
fibonacci=[]
while a <= n2:
    if a >= n1:
        fibonacci.append(a)
    a,b=b,a+b
if fibonacci:
    print(f"fibonacci series between {n1} and {n2} is :")
    print(fibonacci)
else:
    print(f"No fibonacci number found between {n1} and {n2}")