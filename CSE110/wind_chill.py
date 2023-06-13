#Formula
#Wind Chill (F) = 35.74 + 0.6215(Air Temprature) - 35.75((WIndspeed)**0.16) + 0.4275(Airtemprature)((WIndspeed)**0.16)

#Function
def calc_windchill(air_temp, wind_speed, temp_unit = "Fahrenheit"):
    '''
    air_temp = float or int
    wind_speed = float or int
    temp_unit = str
    Always returns windchill in Faherheit, accepts Celsius or Fahrenheit.
    '''
    
    if temp_unit[0].upper() == "C":
        air_temp = (air_temp * (9/5)) +32
    
    else:
        pass
    
    windchill = 35.74 + (0.6215 * air_temp) - 35.75 * (wind_speed**0.16) + (0.4275 * air_temp * (wind_speed**0.16))
    return round(windchill, 2)


temp = float(input("What is the air temprature? "))
#speed = float(input("What is the air speed? "))
unit = input("What unit of measurment do you wish to use? (F/C -SKIP to skip this step) ")

#if temp_unit.upper != "SKIP":
#    print(calc_windchill(temp, speed, temp_unit))
#else:
#    print(calc_windchill(temp, speed))

print("")

for i in range(1,13):
    air_speed = 5 * i

    windchill = calc_windchill(temp, air_speed, unit)
    
    print(f"At {temp} degrees and {air_speed} mph, the windchill is {windchill} Fahrenheit.")
        