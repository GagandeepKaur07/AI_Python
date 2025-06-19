 #task4 Implementation of List all files and directories
import os
directory_path='.'
contents=os.listdir(directory_path)
print(f"Content of {directory_path}':")
for item in contents:
    print(item)