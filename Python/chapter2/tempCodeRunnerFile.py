#task 1 :To Opening a file in write mode ('w')
# file = open('example.txt','w')
# file.write("Hello,world \n this is the test file.")
# file.close()

# # Task 2: Opening a file in read mode ('r')
# file = open('example.txt','r')
# content=file.read()
# print("full content:")
# print(content)

# file.close()

# # Task 3: Opening the file again to read line by line
# file=open('example.txt','r')
# print("Reading all lines at once:")
# lines=file.readlines()
# for line in lines:
#     print(line,end='')
# file.close()

# # Task 5 : Opening a file in append mode ('a') 
# file=open('exaple.txt','a')
# file.write("\n Appending a new line to the file.")
# file.close()

# # Task 6: Using with statement to automatically close the file 
# with open('example.txt','r') as file:
#     content = file.read()
#     print("contentusing 'with statement :")
#     print(content)

# # Task 7: File Pointer Management 
# with open('example.txt','r') as file:
#     print("initial pointer position :",file.tell())
#     file.read(5)
#     print("pointer position after reading 5 character:",file.tell())

#     file.seek(0)
#     print("pointer position after seek(0):",file.tell())

#     content=file.read()
#     print("content after seek (0):")
#     print(content)