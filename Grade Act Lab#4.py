def assign_grade():
    marks = int(input("Say your Grade:"))
    if marks <= 0:
        print("Invalid score! Please enter a value between 0 and 100.")
    if marks >= 101:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
        
assign_grade()

                