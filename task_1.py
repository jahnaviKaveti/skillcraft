def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
  """Converts Celsius to Kelvin."""
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
  """Converts Fahrenheit to Kelvin."""
  return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
  """Converts Kelvin to Celsius."""
  return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
  """Converts Kelvin to Fahrenheit."""
  return (kelvin - 273.15) * 9/5 + 32

# Get user input
temperature = float(input("Enter the temperature: "))
scale = input("Enter the original scale (C, F, or K): ").upper()

# Convert the temperature
if scale == "C":
  fahrenheit = celsius_to_fahrenheit(temperature)
  kelvin = celsius_to_kelvin(temperature)
  print("Fahrenheit: ", fahrenheit)
  print("Kelvin: ", kelvin)
elif scale == "F":
  celsius = fahrenheit_to_celsius(temperature)
  kelvin = fahrenheit_to_kelvin(temperature)
  print("Celsius: ", celsius)
  print("Kelvin: ", kelvin)
elif scale == "K":
  celsius = kelvin_to_celsius(temperature)
  fahrenheit = kelvin_to_fahrenheit(temperature)
  print("Celsius: ", celsius)
  print("Fahrenheit: ", fahrenheit)
else:
  print("Invalid scale.")