# 1. Creating a Dictionary
# Task 1  Implementation of Creating a Dictionary
student_grade={
    "gagan":85,
    "bittu":78,
    "deep":62
    }
print("Student Grade :", student_grade)

# Task 2 : Implementation of Accessing Dictionary Values
grade=student_grade["deep"]
print("deep's grade :" ,grade)

# Task 3 :  Implementation of Adding a New Key-Value Pair
student_grade["Rashmi"]=88
print("update Student Grade :", student_grade)

# Task 4 : Implementation of Removing a Key-Value Pair
student_grade.pop("deep")
print("Student Grades after removing Soumya :", student_grade)

# Task 5 : Implementation of checking Membership
is_charlie_in_dict="Rashmi" in student_grade
print("is charlie in te dictionary ?" , is_charlie_in_dict)

# Task 6 : Implementation of Removing a Key-Value Pair
print("Iterating over students names and grades : ")
for student, grade in student_grade.items():
    print(f"{student}:{grade}")

# Task 7 : Implementation of Using the get() Method
david_grade=student_grade.get("bittu","Not found")
print("bittu's grade :", david_grade)

# Task 8 : Implementation of Merging Dictionaries
additional_grade={"Bhawani":60,"Usha":75}
student_grade.update(additional_grade)
print("Student grade after merging with additional data : ", student_grade)

# Task 9 :  Implementation of Dictionary Comprehension
squared_numbers= {x:x **2 for x in range(1,11)}
print("Dictionary of numbers and their square :", squared_numbers)

# Task 10 : Implementation of Handling Nested Dictionaries
nested_dict={
    "USA":{"New york":8000000,"Los Angeles":4000000},
    "India":{"Mumbai":20000000, "Delhi":15000000}
}
print("Nested dictonary of countries and citites :",nested_dict )

my_population=nested_dict["USA"]["New york"]
print("Populion of New York:",my_population)

# Task 11 : Implementation of Clearing and Copying Dictionaries
student_grade_copy = student_grade.copy()
print("copy of student grade:",student_grade_copy)

student_grade.clear()
print("Student grade after clearing:", student_grade)
