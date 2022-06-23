

class Class_level:
    def __init__(self, f_name, l_name, major, year, gpa,id):
        self.__f_name = f_name#first name get 
        self.__l_name = l_name#last name get 
        self.__major = major#major get 
        self.__year = year#year (freshman, sophmore, junior senior) get 
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
    
    def get_year(self):
        return self.__year
    
    def set_year(self, new_year):
        self.__year = new_year
    
    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa
    
    def get_id(self):
        return self.__id