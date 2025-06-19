hp =65000
apple = 75000
acer = 80000

# Cheapest
    
print("Cheapest:-")
if apple < hp and apple < acer:
    print("Apple: ",apple)
elif hp < apple  and hp < acer:
    print("HP: ",hp)
else:
    print("Acer", acer)

# Expensive
print("Expensive:-")
if apple > hp and apple > acer:
    print("Apple: ",apple)
elif hp > apple  and hp > acer:
    print("HP: ",hp)
else:
    print("Acer", acer)
