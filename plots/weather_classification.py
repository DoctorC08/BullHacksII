import math

def calculate_feels_like(temp, humidity, wind_speed):
    # Convert temp to Fahrenheit
    temp = temp * 1.8 + 32
    humidity = humidity / 100  # Convert humidity to a fraction
    
    if temp > 80: 
        adjustment = 0
        heat_index = -42.379 + 2.04901523 * temp + 10.14333127 * humidity - 0.22475541 * temp * humidity - 0.00683783 * temp ** 2 - 0.05481717 * humidity ** 2 + 0.00122874 * temp ** 2 * humidity + 0.00085282 * temp * humidity ** 2 - 0.00000199 * temp ** 2 * humidity ** 2
        
        # Apply adjustments for specific conditions
        if (temp > 80 and temp < 112) and (humidity < 0.13):
            adjustment = ((13 - humidity) / 4) * math.sqrt((17 - abs(temp - 95.)) / 17)
        elif (humidity > 0.85) and (temp > 80 and temp < 87):
            adjustment = ((humidity - 0.85) / 10) * ((87 - temp) / 5)
        
        heat_index -= adjustment
        return heat_index
    elif temp > 50:
        heat_index = 0.5 * (temp + 61.0 + ((temp - 68.0) * 1.2) + (humidity * 0.094))
        return heat_index
    else:
        wind_chill = 35.74 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp * (wind_speed ** 0.16)
        return wind_chill
