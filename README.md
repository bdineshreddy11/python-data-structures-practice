# 🐍 Python Data Structures & Conditional Statements
---

## 📌 Overview 
This project focuses on fundamental Python programming concepts used to store, access, modify, and process data.

It covers three core Python data structures along with conditional statements and user input handling.

### Core Areas

* 🟦 **Lists**
* 🟪 **Dictionaries**
* 🟩 **Sets**
* 🟧 **Conditional Statements**
* 🔵 **User Input & Decision Making**

---

## 🛠️ Concepts Covered

| Area                     | Concepts                                                |
| :----------------------- | :------------------------------------------------------ |
| 🟦 **List**              | Creation, modification, indexing, slicing, sorting      |
| 🟪 **Dictionary**        | Key-value pairs, access, add, update, iteration         |
| 🟩 **Set**               | Unique values, union, intersection, immutability        |
| 🟧 **Conditional Logic** | `if`, `elif`, `else`                                    |
| 🔵 **Input Handling**    | `input()`, type conversion, validation, decision making |

---

# 📚 01. List Operations

## Creating Lists

Two lists are created to work with integer and string values.

```python
age_list = [24, 25, 26, 27, 28]

name_list = [
    "Rahul",
    "Priya",
    "Arun",
    "Sneha",
    "Kiran"
]
```

## List Modification

The following built-in methods are practiced:

```text
append()   → Adds an element to the end
insert()   → Adds an element at a specific index
remove()   → Removes a specific value
pop()      → Removes an element
extend()   → Adds multiple elements
sort()     → Arranges elements
```

The list is also used to calculate:

* 🔹 Maximum value
* 🔹 Minimum value
* 🔹 Sum of all values

## List Access

Indexing and slicing are used to access individual elements and ranges.

| Operation         | Purpose                    |
| :---------------- | :------------------------- |
| `name_list[0]`    | First element              |
| `name_list[-1]`   | Last element               |
| `name_list[2:5]`  | Elements from index 2 to 4 |
| `name_list[::-1]` | Reverse order              |

---

# 📖 02. Dictionary Operations

A dictionary is used to store student names and their corresponding marks.

```python
student_marks = {
    "Rahul": 75,
    "Priya": 88,
    "Arun": 69,
    "Sneha": 92,
    "Kiran": 78
}
```

## Dictionary Operations

The following operations are demonstrated:

```text
Access      → Retrieve a student's mark
Add         → Add a new student
Update      → Modify an existing mark
keys()      → Retrieve all keys
values()    → Retrieve all values
items()     → Retrieve key-value pairs
```

### Example

```python
student_marks["Rahul"]

student_marks["Janani"] = 80

student_marks["Rahul"] = 82

student_marks.keys()
student_marks.values()
student_marks.items()
```

---

# 🔤 03. Set Operations

A set is created using repeated vowel values.

```python
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
```

## Set Behaviour

Sets automatically remove duplicate values.

The repeated `'a'` and `'i'` values therefore appear only once.

```text
Input:
a, e, i, o, u, a, a, i

Unique values:
a, e, i, o, u
```

> **Key Concept:** A set stores unique elements and does not preserve duplicate values.

---

## 🔒 Set Immutability

An attempt is made to modify a set using index-based assignment:

```python
my_set[4] = 's'
```

This produces a `TypeError`.

Sets do not support indexing or index-based assignment because they are unordered collections.

---

## 🔄 Union & Intersection

Two sets are used for comparison:

```python
set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}
```

### Union

```python
set1.union(set2)
```

Returns all unique elements from both sets.

### Intersection

```python
set1.intersection(set2)
```

Returns only the elements common to both sets.

### Results

| Operation           | Result                      |
| :------------------ | :-------------------------- |
| 🔄 **Union**        | `{1, 2, 3, 5, 7, 8, 9, 10}` |
| 🔗 **Intersection** | `{3, 5}`                    |

---

# ⚙️ 04. Conditional Statements

A performance categorization program is implemented using:

```python
if
elif
else
```

The program accepts a score between **0 and 10** and determines the corresponding performance category.

## Performance Logic

| Score Range | Category         |
| :---------: | :--------------- |
|    `> 7`    | 🟢 Above Average |
|   `4 – 7`   | 🟡 Average       |
|    `< 4`    | 🔴 Below Average |

### Example Logic

```python
if score > 7:
    print("Above Average")
elif score >= 4:
    print("Average")
else:
    print("Below Average")
```

The program also displays a supporting message based on the category.

### Sample Output

```text
Enter your score (0 to 10): 7

Average: Good effort! Keep practicing,
there's room for improvement.
```

---

# 🧠 Python Skills Practiced

```text
                    Python Fundamentals
                           │
          ┌────────────────┼────────────────┐
          │                │                │
        Lists        Dictionaries          Sets
          │                │                │
     ┌────┼────┐      ┌────┼────┐      ┌────┼────┐
  Indexing Methods   Access Update    Union Intersection
  Slicing  Sorting   keys() values    Unique Values
                           │
                           ▼
                  Conditional Statements
                           │
                    ┌──────┼──────┐
                    │      │      │
                   if     elif    else
```

---

# 📂 Project Structure

```text
Python-Data-Structures/
│
├── Python_Data_Structures.py
│
└── README.md
```

---

# 🎯 Learning Focus

This project strengthens the Python fundamentals required for data processing and logical problem solving.

### Key Takeaways

* Understand how lists store and manipulate collections
* Use indexing and slicing to access list elements
* Work with dictionary key-value pairs
* Add and update dictionary data
* Retrieve dictionary keys, values, and items
* Understand how sets handle unique values
* Perform union and intersection operations
* Understand set immutability
* Apply `if`, `elif`, and `else`
* Accept and process user input
* Build simple decision-making programs

---

# 🐍 Python

This project is developed using **Python** and focuses on fundamental programming concepts that are useful for data analysis and data processing.

---

<p align="center">
  <b>Python • Data Structures • Logical Thinking • Problem Solving</b>
</p>
