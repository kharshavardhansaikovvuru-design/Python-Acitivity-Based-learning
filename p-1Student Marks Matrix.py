students = ["Arun", "Bhanu", "Charan", "Divya", "Esha"]

subjects = ["Python", "C", "Mathematics", "English"]

marks = [
    [85, 78, 92, 88],
    [72, 80, 75, 70],
    [90, 95, 89, 92],
    [40, 45, 35, 50],
    [65, 70, 60, 75]
]

number_of_students = len(students)
number_of_subjects = len(subjects)

totals = []
averages = []

print("STUDENT-WISE ANALYSIS")
print("-" * 45)

for i in range(number_of_students):
    total = sum(marks[i])
    average = total / number_of_subjects

    totals.append(total)
    averages.append(average)

    print(
        students[i],
        "Total =", total,
        "Average =", round(average, 2)
    )

highest_total = max(totals)
top_index = totals.index(highest_total)

print("\nTOP-PERFORMING STUDENT")
print("Name:", students[top_index])
print("Total Marks:", highest_total)

print("\nSUBJECT-WISE ANALYSIS")
print("-" * 45)

low_performing_subjects = []

for j in range(number_of_subjects):
    subject_total = 0

    for i in range(number_of_students):
        subject_total += marks[i][j]

    subject_average = subject_total / number_of_students

    print(
        subjects[j],
        "Average =", round(subject_average, 2)
    )

    if subject_average < 50:
        low_performing_subjects.append(subjects[j])

print("\nLOW-PERFORMING SUBJECTS")

if len(low_performing_subjects) > 0:
    for subject in low_performing_subjects:
        print(subject)
else:
    print("No low-performing subjects")

print("\nAnalysis completed successfully.")
