# Sets (Operations):
#a. Create a set called my_set with following values: ['a','e','i','o','u','a','a','i'] Analyse the output and provide explanation for the same.
my_set = set(['a','e','i','o','u','a','a','i'])
print("my_set:", my_set)

# b. Attempt to change the value of my_set[4] = 's'. If code throws an error, providean explanation.
""" my_set[4] = 's'  
      This will throw a TypeError because sets are unordered and do not support indexing.
"""
 
 #c. Create two sets:
#set1 with values: {1, 3, 5, 7, 9}
#set2 with values: {2, 3, 5, 8, 10}
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

#d. Compute and print the union and intersection of set1 and set2.
union = set1.union(set2)
intersection = set1.intersection(set2)
print("Union of set1 and set2:", union)
print("Intersection of set1 and set2:", intersection)

