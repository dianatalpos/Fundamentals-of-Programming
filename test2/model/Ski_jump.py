import random

class Ski_jump(object):
    
    
    def __init__(self, name, time, average_speed, wind):
        self.__name = name
        self.__time = time
        self.__average_speed = average_speed
        self.__wind = wind
        self.__distance = time * (average_speed + random.uniform(-0.5, 0.5) * average_speed + wind )

    def __lt__(self, value):
        return self.get_distance() < value.get_distance()

    def get_distance(self):
        '''
        Returns the distance 
        '''
        return self.__distance


    def get_name(self):
        '''
        Returns the name
        '''
        return self.__name


    def get_time(self):
        return self.__time


    def get_average_speed(self):
        return self.__average_speed


    def get_wind(self):
        return self.__wind
    
    def __str__(self):
        return self.get_name() + ", " + str(self.get_distance())

    name = property(get_name, None, None, None)
    time = property(get_time, None, None, None)
    average_speed = property(get_average_speed, None, None, None)
    wind = property(get_wind, None, None, None)
    distance = property(get_distance, None, None, None)
    



