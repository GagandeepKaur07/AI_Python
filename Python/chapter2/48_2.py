# Task 2: Implementation of Rename the directory
import os 
current_name='new_directory'
new_name='renamed_directory'

os.rename(current_name,new_name)
print(f"Directory renamed from'{current_name}' to '{new_name}'.")