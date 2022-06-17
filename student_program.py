from fileinput import close
from subprocess import check_output
#from tkinter.tix import Tree
 
 
file = open("users.txt")
print(" 1. Login\n 2. Create Account\n")
 


out_of_program = True
logged_out = True
making_account = True
while out_of_program:
    choice = input("Enter your choice: ")
    if choice == "1":   #user wants to login
        file = open("users.txt")
        while logged_out:
            entered_username = input("Please enter your username (4-16)")
            entered_password = input("Please enter your password (6-16)")
            #search the lines
            for line in file:
                credentials = line.split(",")
                if(entered_username == credentials[0] and entered_password == credentials[1].rstrip()):
                    print("logged in!")
                    logged_out = False
                    out_of_program = False
    
    
    
    elif choice == "2":
        while making_account:
            wanted_username = input("Please enter a username (4-16)")
            wanted_password = input("Please enter a password (6-16)")
            if((len(wanted_password) >= 6 and len(wanted_password) <=16) and (len(wanted_username) >= 4 and len(wanted_username) <= 16)):
                print("Account created!")
                file = open("users.txt", "a")
                file.write(f"{wanted_username},{wanted_password}\n")
                making_account = False
                out_of_program = False
            else:
                print("please make your credentials fit the specified length")
    else:
        print("Please enter 1 or 2")
file.close()
print("ready to go")

number_of_students = int(input("How many students do you have? "))
student_names = []
student_raw_grades = []
student_grades = []
for iteration in range(number_of_students):
    student_names.append(input("Enter their name: "))
    student_raw_grades.append(float(input("Enter their grade (percentage)")))
for item in student_raw_grades:
    if item >= 90:
        student_grades.append("A")
    elif item >= 80:
        student_grades.append("B")
    elif item >= 70:
        student_grades.append("C")
    elif item >= 60:
        student_grades.append("D")
    elif item >= 50 or item < 50:
        student_grades.append("F")
i = 0
for item in student_names:
    print(f"{item}: {student_grades[i]}")
    i = i + 1
class_average = 0
sum = 0
for item in student_raw_grades:
    sum = sum + item
    class_average = sum/number_of_students
print(f"Class average is: {class_average}")
    
