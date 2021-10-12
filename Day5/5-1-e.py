# Average Height

# taking inputs  heights of students and splitting them as a list
student_heights = input("Input a list of student heights ").split()
# empty var to store total len of student list
count = 0
# empty var to store total sum of students list
sum_of_heights = 0
# getting len of total students in a list by iterating list
for height in student_heights:
    count += 1  # adding 1 for each item in the list.

# sum of the students height by iterating list
for height in student_heights:
    # each item will added to it's sum to the given variable
    sum_of_heights += float(height)
#  printing the Average height in given students list by rounded to int
print(round(sum_of_heights / count))
