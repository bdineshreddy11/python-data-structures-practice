#Dictionary (Creation, Modification and Access):
#a. Create a dictionary named student_marks that maps the names of five students to their marks (use scale of from 0 to 100).
student_marks = {"ramu": 85, "rajesh": 90, "dinesh": 78, "manikanta": 92, "ganesh": 88}
print("Student Marks Dictionary:", student_marks)
#b. Access and print the mark of a specific student, of your choice.
print("Mark of ramu:", student_marks["ramu"])
#c. Add a new student "Janani" with a mark of 80 to the student_marks dictionary.
student_marks["Janani"] = 80
print("Student Marks Dictionary after adding Janani:", student_marks)
#d. Update the mark of any one older student to 82.
student_marks["rajesh"] = 82
print("Student Marks Dictionary after updating rajesh:", student_marks)
#e. Use the keys(), values(), and items() methods to print all keys, values, and key-value pairs in the student_marks dictionary.
print("Keys:", list(student_marks.keys()))
print("Values:", list(student_marks.values()))
print("Key-Value pairs:", list(student_marks.items()))