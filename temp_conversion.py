
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
unit = unit.upper()
temp = float(input("Enter the temperature: "))

if unit == "C": #convert with (C * 9/5) + 32
    temp = round((9 * temp)/ 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} degrees F")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
else:
    print(f"{unit} is an invalid unit of measurement")