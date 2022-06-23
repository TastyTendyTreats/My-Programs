from Student import Class_level

def print_data(student):
    print("\nStudent Data")
    print(student.get_f_name())
    print(student.get_l_name())
    print(student.get_major())
    print(student.get_year())
    print(student.get_gpa())
    print(student.get_id())

def main():
    student1 = Class_level("Ian", "Madden", "Computer Science", "Junior", "4.0", "218802")
    student1.set_major("Introduction to Python")
    
    print_data(student1)


main()