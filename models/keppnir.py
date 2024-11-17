
class Keppnir:
    def __init__(self, year, country, city, location, broadcaster, date):
        self.__year = year
        self.__country = country
        self.__city = city
        self.__location = location
        self.__broadcaster = broadcaster
        self.__date = date

    def get_year(self):
        return self.__year
    
    def get_country(self):
        return self.__country
    
    def get_city(self):
        return self.__city
    
    def get_location(self):
        return self.__location
    
    def get_broadcaster(self):
        return self.__broadcaster
    
    def get_date(self):
        return self.__date