'''# Task 1
t1=(1,2,3)
t2='a','b','c'
t3=tuple([4,5,6])
print( t1 , t2 , t3 )

# Task 2
my_tuple=(10,20,30,40)
print(my_tuple[0])
print(my_tuple[2])

# Task 3 implementation of slicing a tuple
my_tuple=(1,2,3,4,5,6)
print(my_tuple[1:4])
print(my_tuple[1::2])

# Task 4 explanation of Immutable in tuple
my_tuple=(1,2,3)
#my tuple [10]=10
print('tuple are immutable')

# Task 5 implementtation of concatenating Tuple
t1=(1,2)
t2=(3,4)
result=t1+t2
print(result)'

# Task 6 implementation of repeating a tuple
my_tuple=(1,2)
repeated=my_tuple*3
print(repeated)

# Task 7 implementation of finding the lengh of a tuple
my_tup=(10,20,30)
print(len(my_tup))

# Task 8  Implementation of Checking Membership in a Tuple
my_tuple=(1,2,3)
print(2 in my_tuple)
print(4 in my_tuple)

# Task 9  Implementation of Iterating Over a Tuple
my_tuple=(1,2,3)
for item in my_tuple:
    print(item)

#Task 10: Implementation of Finding the Index of an Element in a Tuple
my_tuple = (10,20,30)
print(my_tuple.index(20))

# Task 11: Implementation of Counting Occurrences of an Element in a Tuple python
my_tuple=(1,2,2,3,2)
print(my_tuple.count(2))

#Task 12: Explanation of Nested Tuples
nested_tuple=(1,(2,3),(4,(5,6)))
print(nested_tuple[1])
print(nested_tuple[2][1])

#Task 13: Implementation of Unpacking a Tuple
my_tuple=(1,2,3)
a,b,c=my_tuple
print(a,b,c)

#Task 14: Usage of Tuples as Dictionary Keys
coordinates={(1,2):"point A",(3,4):"point B"}
print(coordinates[(1,2)])

# Task 15: Comparison of Tuples with Lists
my_tuple=(1,2,3)
my_list=[1,2,3]
#my_tuple[0] = 10
my_list[0]=10
print(my_list)

# Task 16: Use of Tuples in Returning Multiple Values from a Function
def get_coordinates():
    return(10,20)
x,y=get_coordinates()
print(x,y)

# Task 17: Implementation of Sorting a List of Tuples
tuple=[(3,'C'),(1,'A'),(2,'B')]
sort=sorted(tuple)
print(sort)'''

# Task 18: Explanation of Hashability in Tuples
my_tuple=(1,2,3)
print(hash(my_tuple))

# Task 19 : Demonstration of Tuple Packing and Unpacking in a Function
def pack(*args):
    return args
packed=pack(1,2,3)
print(packed)

# Task 20 : Conversion Between Lists and Tuples
my_list=[1,2,3]
my_tuple=tuple(my_list)
converted_list=list(my_tuple)
print(my_tuple,converted_list)