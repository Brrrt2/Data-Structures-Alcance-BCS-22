passed = 0
failed = 0

student = [['Name', 'Quiz1', 'Quiz2', 'Quiz3', 'Class Participation', 'Exam', 'Final Grade', 'Status']]

while True:
    name = input("Enter Name: ")
    q1 = input("Enter Quiz 1: ")
    q2 = int(input("Enter Quiz 2: "))
    q3 = input("Enter Quiz 3: ")
    cp = input("Enter Class participation:")
    exam = input("Enter Final Exam: ")

    qtotal = (float(q1) + float(q2) + float(q3)) / 3
    grade = (float(qtotal) * .40) + (float(exam) * .40) + (float(cp) * .20)
    print(f"Final grade: {grade}")

    if grade > 75:
        status = "Passed"
        print("Status: Passed")
    elif grade < 75:
        status = "Failed"
        print("Status: Failed")

    record = [name, q1, q2, q3, cp, exam, grade, status]
    userinput = input("Do you want to continue?(yes/no):")

    if userinput.lower() in ["yes", "Yes"]:
        student.append(record)
        continue

    elif userinput.lower() in ["no", "No"]:
        student.append(record)
        column_widths = [max(len(str(item)) for item in column) for column in zip(*student)]
        header = student[0]
        print("|".join(f"{header[i]:{column_widths[i]}}" for i in range(len(header))))
        separator = ["-" * width for width in column_widths]
        print("|".join(separator))
        for row in student[1:]:
            print("|".join(f"{row[i]:{column_widths[i]}}" for i in range(len(row))))

        break
    else:
        print("Error... Try again later")
        break

for column in range(len(student)):
    if student[column][7].lower() == "passed":
        passed = passed + 1
        continue
    elif student[column][7].lower() == "failed":
        failed = failed + 1
        continue
    else:
        continue

print("==============================================================================")
print(f"Number of Student Passed: {passed}")
print(f"number of Student Failed: {failed}")