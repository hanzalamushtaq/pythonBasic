#Ek IoT weather monitoring system mein __temperature
# ki value ko system ke bahar display karna hai,
#lekin use koi change na kar sake. Is temperature ko 
# safe tarike se print karne ke liye getter method 
#get_temperature() kaise likhenge?

class Weather:
    __temperature = 0.0  # Private attribute

    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature
    
w1=Weather(25.5)
print(w1.get_temperature())