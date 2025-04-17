def calculate_grade():
    # Ask how many lessons the user has?
    while True:
        try:
            num_lessons = int(input("How many lessons do you have? "))
            if num_lessons <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Get grades for each lesson?
    grades = []
    for i in range(num_lessons):
        while True:
            try:
                grade = float(input(f"Enter grade for lesson {i+1} (0-20): "))
                if 0 <= grade <= 20:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 20.")
            except ValueError:
                print("Please enter a valid number.")

    # Calculate average?
    average = sum(grades) / len(grades)

    # Determine letter grade?
    if 18 <= average <= 20:
        letter_grade = "A"
    elif 15 <= average < 18:
        letter_grade = "B"
    elif 12 <= average < 15:
        letter_grade = "C"
    else:
        letter_grade = "F"

    # Print results
    print(f"\nYour average grade is: {average:.2f}")
    print(f"Your letter grade is: {letter_grade}")
    

# Run the function
calculate_grade()
