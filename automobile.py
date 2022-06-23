from datetime import date
class Automobile:

    def __init__(self, make, model, vin, color, year):
        #set automobile attributes
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__color = color
        self.__year = year
    #create get and set methods for the class attributes
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        self.__color = new_color
    
    def get_year(self):
        return self.__year
    
    def get_age(self):
        todays_date = date.today()
        this_year = todays_date.year
        return this_year - self.__year

    def honk_horn(self, number_of_honks):
        honk_string = ""
        for item in range(number_of_honks):
            honk_string = honk_string + "Honk! "
        
        print(honk_string)