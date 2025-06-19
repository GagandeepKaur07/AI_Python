x=[1,2,3]
y=[1,2,3]
z=x

print(f"x is y :{x is y}")
print(f"x is z; {x is z}")
print(f"x is not: {x is not y}")
print(f"x is not: {x is not z}")

#Membership
seq=[1,2,3,4,5]
val=3
NI=10

print(f"{val in seq}")
print(f"{NI in seq}")
print(f"{val not in seq}")
print(f"{NI not in seq}")

St="hello,World!"
ch='h'
CN='x'

print(ch in St)
print(CN in St)
print(ch not in St)
print(CN not in St)