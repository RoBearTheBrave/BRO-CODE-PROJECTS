# using dictionary comprehensions is very similar to using list comprehensions, but with a few key differences
# dictionary comprehensions = create a dictionary using an expression and a for loop

# create a dictionary of cities and their temperatures
cities = {"New York": 32, "Boston": 75, "Chicago": 69, "Miami": 88}

cities_in_fahrenheit = {key: (value * 9/5) + 32 for (key, value) in cities.items()}
print(cities_in_fahrenheit)

cities_in_celsius = {key: (value - 32) * 5/9 for (key, value) in cities_in_fahrenheit.items()}
print(cities_in_celsius)


# create a dictionary of weather conditions
# weather = {"New York": "snow", "Boston": "sunny", "Chicago": "rain", "Miami": "sunny"}
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather)


# create a dictionary of cities and their temperatures
# use if else to replace the value of the temperature with the description of the weather
def check_temp(value):
    if value >= 70:
        return "hot"
    elif 69 >= value >= 50:
        return "warm"
    else:
        return "cold"

cities = {"New York": 32, "Boston": 75, "Chicago": 69, "Miami": 88}
description = {key: check_temp(value) for (key, value) in cities.items()}
print(description) 