# Task 1
counter=1
while counter<= 5:
    print(counter)
    counter+=1
# Task 2
num=7
guess=0
while guess != num:
    guess = int(input("guess the number bteween 1 to 10 :"))
print("Congratulations! you guessed the correct number.")

# Task 3
num1=10
while num1>0:
    print(num1)
    num1 -=1
    if num1 == 5:
        break 
        
# Task 4
num=0
while num<10:
    num += 1
    if num %2==0:
        continue
    print(num)
while True:
    name=input("Enter your name (Type 'exit' to stop):")
    if name == 'exit':
        break
    print(f"hello, { name} !")
print("loop Exited")