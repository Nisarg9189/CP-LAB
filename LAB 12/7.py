class Weather:
    def __init__(self, weather_params):
        self.weather_params = weather_params

   
    def __contains__(self, item):
        return item in self.weather_params


weather = Weather(['temperature', 'humidity', 'pressure', 'wind speed', 'rainfall'])


print('temperature' in weather)  
print('sunlight' in weather)     
print('rainfall' in weather)     
print('cloud cover' in weather)  
print('wind speed' in weather)   