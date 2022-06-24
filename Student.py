

class Student:
    def __init__(self, f_name, l_name, major, credit_hours, gpa,id):
        self.__f_name = f_name#first name get 
        self.__l_name = l_name#last name get 
        self.__major = major#major get 
        self.__credit_hours = credit_hours#year (freshman, sophmore, junior senior) get 
        self.__gpa = gpa#gpa get 
        self.__id = id#ID Number

    def get_f_name(self):
        return self.__f_name
    
    def set_f_name(self, new_f_name):
        self.__f_name = new_f_name

    def get_l_name(self):
        return self.__l_name
    
    def set_l_name(self, new_l_name):
        self.__l_name = new_l_name

    def get_major(self):
        return self.__major
    
    def set_major(self, new_major):
        self.__major = new_major
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_credit_hours):
        self.__credit_hours = new_credit_hours

    def get_class_level(self):
        if(self.__credit_hours < 30):
            return "Freshman"
        elif (self.__credit_hours < 60):
            return("Sophomore")
        elif(self.__credit_hours < 90):
            return ("Junior")
        else:
            return ("Senior")
    
    def update_hours(self, new_hours):
        self.__credit_hours += new_hours

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa
    
    def get_id(self):
        return self.__id