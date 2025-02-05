def main():
    temperature = float(input("Enter the temperature: "))
    unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").upper()

    if unit == 'C':
        result = celsius_to_fahrenheit(temperature)
        original_unit = "°C"
        converted_unit = "°F"
    elif unit == 'F':
        result = fahrenheit_to_celsius(temperature)
        original_unit = "°F"
        converted_unit = "°C"
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return

    print(f"{temperature}{original_unit} is {result:.2f}{converted_unit}")



def celsius_to_fahrenheit(celsius):
    # Celsius to Fahrenheit conversion function
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    # Fahrenheit to Celsius conversion function
    return (fahrenheit - 32) * 5/9




main()
