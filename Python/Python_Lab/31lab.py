num=int(input("Enter a number to create its multiplication table : "))
print(f"multipication table for {num} :")
for i in range(1,11):
    result = num*i
    print(f"{num} X {i} = {result}")