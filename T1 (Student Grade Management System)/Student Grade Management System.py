"""
Name : George Malak Magdy
Date : 19 / 2 /2024
Course : GDG On Campus DMU ML Track
NO Task : 1
"""
# function to check from user`s input for grade
def checker():
    while True:
        try:
            num = float(input("Enter a number (between 0 and 100): "))
            if (0 <= num and num <= 100):
                return num
            else:
                print("Error NO! The number must be between 0 and 100.")
        except ValueError:
            print("Invalid input ! Please enter a valid integer or float number.")

# Function to enter all Students and their Grades
def col_dat():
    st = {}
    while True:
        name = input("Enter Student's name (or enter 'done' to finish): ")
        if name.lower() == 'done':
            break
        else:
            grad = checker()
            st[name] = grad
    return st

# Extract the highest and lowest Student & average of all students
def calc(st):
    if not st:
        return None, None, None
    count = 0
    sm = 0
    mx = float('-inf')
    mn = float('inf')
    Hst = ""
    Lst = ""
    for name, grad in st.items():
        sm += grad
        count += 1
        if grad > mx:
            mx = grad
            Hst = name
        if grad < mn:
            mn = grad
            Lst = name
    avg = sm / count
    return avg, (Hst,mx), (Lst,mn)

# Help with print Grade
def evalgr(grad):
    if grad >= 90:
        return "Excellent"
    elif (grad >= 75 and grad <= 89):
        return "Good"
    else:
        return "Needs improve"


# Display Average , lowest , highest and students with their grades
def disp(st):
    av, high, low = calc(st)
    print("\nClass Performance Report")
    print("-" * 25)
    print(f"Total Students: {len(st)}")
    print(f"Average Grade: {av:.2f}")
    print(f"Highest Grade: {high[1]} - ({high[0]})")
    print(f"Lowest Grade: {low[1]} - ({low[0]})")
    print("\nPerformance Breakdown:")
    for name, grade in st.items():
        print(f"{name} - {grade} ({evalgr(grade)})")

# Starting of Prog
print("### Welcome to Student Grade Management !! ###\n")
student = col_dat()
disp(student)
