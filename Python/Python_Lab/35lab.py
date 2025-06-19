# Task 1
set_a={1,2,3,4,5}
set_b={4,5,6,7,8}
print("set A ;",set_a)
print("set B :", set_b)

# Task 2 :
set_a.add(6)
set_a.remove(1)
print("Set A after 6 and removing 1 :",set_a)

# Task 3 : Implementation of Union of Sets
union_set=set_a.union(set_b)
print("union of A and B :",union_set)

# Task 4 : Implementation of Intersection of Sets
intersection_set= set_a.intersection(set_b)
print("Intersection of Set A and B :", intersection_set)

# task 5 : Implementation of Difference of Sets
difference_set=set_a.difference(set_b)
print("difference : (A-B)", difference_set)

# Task 6 : Implementation of Symmetric Difference of Sets
sym_diff_set=set_a.symmetric_difference(set_b)
print("symmetric diference : ", sym_diff_set)

# Task 7 :  Implementation of Subset and Superset Testing
set_c={4,5}
is_subset=set_c.issubset(set_a)
is_superset=set_a.issuperset(set_c)
print(f" is set c a subset of a : {is_subset}")
print(f" is set A is supersubset of C : {is_superset}")

# Task 8 : Implementation of Set Membership Testing
is_member=3 in set_a
print("is 3 in set A :",is_member)

# Task 9 :: Implementation of Removing Duplicates Using Sets
number_list=[1,2,3,4,4,5,6,6,7]
unique_number= set(number_list)
print("list of number after removing duplicates",unique_number)

#Task 10: Implementation of Set Comprehension
squares_set={x**2 for x in range (1,11)}
print("set of square of number from from 1 to 0 :",squares_set)

# Task 11 :
set_a.clear()

