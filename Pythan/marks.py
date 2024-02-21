def main():
    try:
        marks = float(input("Enter the marks obtained: "))
        if 0 <= marks <= 100:
            grade = calculate_grade(marks)
            print(f"The grade for {marks} marks is: {grade}")
        else:
            print("Invalid input. Marks should be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

def calculate_grade(marks):
    if marks < 50:
        return "Fail"
    elif 50 <= marks < 60:
        return "Pass"
    elif 60 <= marks < 70:
        return "Grade D"
    elif 70 <= marks < 80:
        return "Grade C"
    elif 80 <= marks < 90:
        return "Grade B"
    elif 90 <= marks <= 100:
        return "Grade A"
    else:
        return "Invalid input. Marks should be between 0 and 100."