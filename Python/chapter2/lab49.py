import json
import os

# file to store library data
LIBRARY_FILE='library_data.json'

# Function to load library data from a file
def load_library():
    if not os.path.exists(LIBRARY_FILE):
        return{}
    try:
        with open(LIBRARY_FILE,'r') as file:
            return json.load(file) 
    except Exception as e:
        print(f"Error loading library data: {e}")
        return{}

# Function to save library data to a file
def save_library(library):
    try:
        with open(LIBRARY_FILE,'w') as file:
            json.dump(library,file)
    except Exception as e:
        print(f"Error saving library data:{e}")

#Task 3: Function to add a book to the library 
# function to add a book to the library
def add_book(Library,Title,Author,Quantity):
    if Title  in Library:
        print("Book already exists. Updating the quantity.")
        Library[Title]['Quantity'] +=Quantity
    else: 
        Library[Title]={'Author':Author,'Quantity':Quantity,'borrowed_by':None}
    save_library(Library)
    print(f"Book '{Title}' added successfully!")

# Task 4: Function to view all books in the library
def view_books(Library):
    if not Library:
        print("The library is empty.")
        return
    for Title,details in Library.items():
        status =f"Available ({details['Quantity']})" if not details['borrowed_by'] else f"borrowed_by {details ['borrowed_by']}"
        print(f"Ttile: {Title}, Author: {details['Author']},Status:{status}")

# Task 5: Function to borrow a book from the library

#function to borrow a book from the library
def borrow_book(Library,Title,borrower_name):
    if Title not in Library:
        print("Book not found in the library.")
        return
    if Library[Title]['Quantity']==0:
        print(f"All copies of '{Title}' are currenly borrowed.")
        return
    if Library[Title]['borrowed_by']:
        print(f"The book '{Title}' is currently borrowed by {Library[Title]['borrowed_by']}.")
        return
    Library[Title]['Quantity']-=1
    Library[Title]['borrowed_by'] =borrower_name
    save_library(Library)
    print(f"'{Title}' has been borrowed by {borrower_name}.")

#Task 6: Function to return a borrowed book to the library
 
 #function to return a borrowed book to the library
def return_book(Library,Title):
    if Title not in Library:
        print("book not found in the library.")
        return
    if not Library[Title]['borrowed_by']:
        print(f" The book '{Title}' was not borrowed.")
        return
    Library[Title]['Quantity'] +=1
    borrower_name=Library[Title]['borrowed_by']
    Library[Title]['borrowed_by']=None
    save_library(Library)
    print(f"'{Title}' has been returned by {borrower_name}")


# Task 7: Main function to run the Library Management System

#main function to run the library management system
def main():
    Library = load_library()
    while True:
        print("\n library managemnt system")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your Choice :")
        if choice == '1':
            Title = input("Enter the book title :")
            Author=input("Enter the book Author :")
            try:
                Quantity=int(input("Enter the Quantity of the book :"))
                add_book(Library,Title,Author,Quantity)
            except ValueError:
                print("Invalid input for the Quantity. Please enter an integer")
        elif choice == '2':
            view_books(Library)
        elif choice == '3':
            Title=input("Enter the book title: ")
            borrower_name= input("Enter your Name")
            borrow_book(Library, Title, borrower_name)
        elif choice == '4':
            Title= input("Enter the book title: ")
            return_book(Library,Title)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__=="__main__":
    main()

