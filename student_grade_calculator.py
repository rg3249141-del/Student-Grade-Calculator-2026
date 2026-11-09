# student grade calculator
# programming fundamentals and logic building using python

# function to calculate total marks
def calculate_total(marks):
    total = sum(marks)
    return total

# function to calculate percentage
def calculate_percentage(total):
    percentage = (total / 500)*100
    return percentage

# function to calculate grade
def calculate_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >=70:
        return "B"
    elif percentage >=55:
        return "C"
    elif percentage >=40:
        return "D"
    else:
        return "F"


# function to validate marks
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input("Enter marks for " + subject + ":"))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invailid marks. Enter a number between 0 and 100.")

        except ValueError:
            print("Invailid marks. Enter a number between 0 and 100.")


# Main program
print("===== STUDENT GRADE CALCULATOR=====")

while True:
    name = input("\nEnter student name:")

    marks = []

    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

    for subject in subjects:
        subject_marks = get_valid_marks(subject)
        marks.append(subject_marks)


    total = calculate_total(marks)
    percentage = calculate_percentage(total)


    # calculate grade and result

    grade = calculate_grade(percentage)

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    # display student result
    print("\n===== STUDENT RESULT =====")
    print("Name:", name)
    print("Total:", format(total, ".2f"))
    print("Percentage:", format(percentage, ".2f") + "%")
    print("Grade:", grade)
    print("Result:", result)


    # ask for another student

    while True:
        choice = input("\nDo you want to enter another student? (y/n):").lower()
        if choice == "y" or choice == "n":
            break
        else:
            print("Please enter y or n.")

            if choice == "n":
                print("\nThank you for using Student Grade Calculator!")
                break




