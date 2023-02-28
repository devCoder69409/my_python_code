def report_weather(temperature, weather_preference):
    return weather_preference(temperature)

def as_sun_lover(temperature):
    if temperature >= 25:
        return "great"
    else:
        return "not great"
    
def as_snow_lower(temperature):
    if temperature <= 0:
        return "great"
    else:
        return "not great"