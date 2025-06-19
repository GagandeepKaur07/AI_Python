# Task 1
fruit = ["apple","banana","cherry","mongo","orange"]
print("Original list :" , fruit)


# Task 2
first=fruit[0]
last=fruit[-1]
print("first ; ", first)
print("last fruit ; ",last)

# Task 3
sublist=fruit[:3]
print("Sublist of First three fruit : ",sublist)

# Task 4
fruit.append("graps")
print("List after adding :",fruit)

# Task 5
fruit.insert(1,"pineapple")
print("list after insert 'pineapple' at position 1 : ",fruit)

# Task 6
fruit.remove("banana")
print("list after removing 'banana' :", fruit)

# Task 7
popped=fruit.pop()
print("popped fruit :", popped)
print("List after popping the last element : ", fruit)

# Task 8
length=len(fruit)
print("numer of fruit in the list : ", length)

# Task 9
list="apple" in fruit
print("is apple in the list ? ", list)

# Task 10
print("iterating over the list :")
for fruit1 in fruit:
    print(fruit1)

# Task 11
fruit.sort()
print("sorted list :")

# Test 12
fruit.reverse()
print("List after reversing the order :", fruit)

# Test 13
fruit2=[fruit3 for fruit3 in fruit if len(fruit)>5]
print("Fruit wwith more than 5 ",fruit2)

# Test 14
fruit_copy=fruit.copy()
print("copied list :", fruit)

# Test 15
fruit.clear()
print("clear list :",fruit)

# Test 16
vegitable=["carrot","broccoli","spinach"]
fruit_copy.extend(vegitable)
print("List after ", vegitable)

# Test 17
num_apples=fruit_copy.count("apple")
print("number of apple in the list :", num_apples)

# Test 18
if "carrot" in fruit_copy:
    carrot_index=fruit_copy.index("carrot")

# Test 19
if len(fruit_copy)>2:
    del fruit_copy[2]
print("list after removing element at index 2 :", fruit_copy)

# Test 20
nested_list= [fruit_copy,vegitable]
print("Nested list :", nested_list)