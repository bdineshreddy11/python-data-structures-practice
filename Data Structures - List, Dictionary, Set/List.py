# 1. List Creation:
age_list = [14,18,22,26,30,34,38]
name = ["rajesh","dinesh","manikanta","ramu","ganesh","rajkumar","harix"]

# 2.List Operations / Modifications:
# a. Append the string "Yazhini" to name_list.
name.append("Yazhini")
print("Name list",name)
#b. Insert the element 30 at index 2 in age_list.
age_list.insert(2,30)
print("Age list",age_list)
#c. Remove the string "Yazhini" from name_list.
name.remove("Yazhini")
print("Name list",name)
#d. Pop the last element from age_list.
age_list.pop()
print("Age list after pop",age_list)
#e. Extend the age_list with additional ages [29, 30, 26].
age_list.extend([29, 30, 26])
print("Age list after extend",age_list)
#f. Sort age_list in descending order.
age_list.sort(reverse=True)
print("Age list after sorting in descending order",age_list)
#g. Find Max age, Min age and sum of all ages from age_list.
age_max = max(age_list)
age_min = min(age_list)
age_sum = sum(age_list)
print("Max age:",age_max)
print("Min age:",age_min)
print("Sum of all ages:",age_sum)
#3. Accessing List Elements:
# a. Print the first element of name_list.
print("First element of name_list:", name[0])
#b. Print the last element of name_list.
print("Last element of name_list:", name[-1])
#c. Print the elements from index 2 to index 4 in name_list.
print("Elements from index 2 to 4:", name[2:5])
#d. Print the elements of name_list in reverse order.
print("Elements of name_list in reverse order:", name[::-1])
