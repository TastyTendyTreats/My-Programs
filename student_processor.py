from Student import Student

#create a function that loads the student data from the students.csv
#create student objects and place in a list
#return a list of student objects

student_dict = {}
student_dict_list = []
def load_students():
    counter = 0
    
    file = open("students.csv")
    list_of_students = []
    for line in file:
        counter += 1
        if counter == 1:
            continue
        arguments = line.split(',')
        if(len(arguments) != 6):
            raise Exception(f"Lack of data in line {counter} in the file")
        else:
            student = Student(arguments[0], arguments[1], arguments[2], int(arguments[3]), float(arguments[4]), arguments[5].rstrip())
            list_of_students.append(student)

    return list_of_students

def make_dict(list_of_students):
    for student in list_of_students:
        student_dict_list.append({
            'id':student.get_id(),
            'name':student.get_f_name() + " " + student.get_l_name(),
            'major':student.get_major(),
            'gpa': student.get_gpa(),
            'class': student.get_class_level()
        })
        
    return student_dict_list

def print_student_data(list_of_students):
    for student in list_of_students:
        print(f"{student.get_f_name()} {student.get_l_name()}: {student.get_major()}")
        print(f"GPA: {student.get_gpa()}")
        print(f"Class: {student.get_class_level()}")
        print(f"ID: {student.get_id()} \n")
    return

def print_dict(student_dict_list):
    for student in student_dict_list:
        print(student)

def sort_list(list_of_students):
    list_of_students.sort(key=lambda the_student: the_student.get_major())
    return list_of_students

def get_student_dictionary():
    student_list = load_students()
    student_dict_list = make_dict(student_list)
    student_list = sort_list(student_list)
    print_dict(student_dict_list)
    return student_dict_list
