#task 1
word="gagandeep"
for letter in word :
    print(letter)

#task 2 
for i in range(7):
    print(i)

#task 3
row =5
for i in range(1,row+1):
    for j in range(i):
        print("*",end=" ")
    print()

#task 4
for i in range(10):
    if i ==5:
        break
    print(i)

#task 5
for i in range (10):
    if i %2==0:
        continue
    print(i)

#task 6
for i in range(5):
    print("__________",i)
else:
    print("Loop complited successfully")