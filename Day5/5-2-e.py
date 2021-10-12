
# taking inputs and turning it into a list var
student_scores = input("Input a list of student scores ").split()
# iterating list with range function between 0 to len of list
for n in range(0, len(student_scores)):
    # list[0] for each list value converting into int
    student_scores[n] = int(student_scores[n])
# Think about the logic before writing code. How can you
# compare numbers against each other to see which one is larger?

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

print(f"The highest score in the class is: {highest_score}")
