# Python temperature converter

temperature = float(input("Enter the temperature: "))
unit = input("Celsius or Fahrenheit? (C or F): ")

if unit == "C":
    temperature2 = (temperature * 1.8) + 32
    print(f"{temperature}° Celsius = {round(temperature2, 1)}° Fahrenheit.")
elif unit == "F":
    temperature2 = (temperature - 32) * 5/9
    print(f"{temperature}° Fahrenheit = {round(temperature2, 1)}° Celsius.")
else:
    print("Invalid unit.")