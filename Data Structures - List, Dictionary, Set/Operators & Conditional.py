# Operators & Conditional Statements : (IF, ELIF, ELSE)
# Performance Category Program:
#1. Prompt user for Input. Score range should be from 0 to 10 (both inclusive).
score = float(input("Enter your score (0-10): "))

#2. Find the performance category based on the input score using following criteria:
#   a. Above Average: Score greater than 7
#   b. Average: Score between 4 and 7(both inclusive)
#   c. Below Average: Score lesser than 4
if score > 7:
    category = "Above Average"
    message = "Keep up the good work!3"
elif 4 <= score <= 7:
    category = "Average"
    message = "Good effort! keep practicing and need improvement."
else:
    category = "Below Average"
    message = "Need to Improve your performance, consistent practice will lead to better results"

#3. Output: Print the Performance category
print("Performance Category:", category)

#4. Additional Step: You can give a prompt of your choice to each category.
print("Message:", message)
