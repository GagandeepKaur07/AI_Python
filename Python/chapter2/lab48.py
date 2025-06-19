# task 1: Implement of create a new directory 
import os 
directory_path='new_direct'
os.makedirs(directory_path,exist_ok=True)
print(f"Directory'{directory_path}'created.")

# Task 2: Implementation of Rename the directory
import os
current_name='new_direct'
new_name='renamed_direct'

os.rename(current_name,new_name)
print(f"Directory renamed from'{current_name}' to '{new_name}'.")

# ask 3: Implementation of Remove the directory and all its contents
# import shutil
# directory_path='renamed_directory'

# task4 Implementation of List all files and directories
import os 
directory_path='.'
contents=os.listdir(directory_path)
print(f"Content of {directory_path}':")
for item in contents:
    print(item)

# task 5 Implementation of Navigating Directories 
import os 
current_direct1=os.getcwd()
print(f"current working directory : {current_direct1}")
os.chdir('..')
print(f"changed working directory to : {os.getcwd()}")

# task 6 : Implementation of Creating and Writing to Files in directory 
file_path='example.txt'
with open(file_path,'r') as file:
    content=file.read()
print(f"Content of '{file_path}' :\n {content}")
