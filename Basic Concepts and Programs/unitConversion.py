# Create a unit converter in Python, which can convert between different units of measurement. Also it should be robust enough to handle invalid inputs gracefully, and convert the huge values without losing precision.

import sys
def convert_length(value, from_unit, to_unit):
    """Convert length between different units."""
    units = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit provided.")
    
    # Convert value to meters first
    value_in_meters = value * units[from_unit]
    
    # Convert from meters to the target unit
    converted_value = value_in_meters / units[to_unit]
    
    return converted_value

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
        elif to_unit == 'Celsius':
            return value
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
        elif to_unit == 'Fahrenheit':
            return value
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
        elif to_unit == 'Kelvin':
            return value
    
    raise ValueError("Invalid unit provided.")

def main():
    print("Welcome to the Unit Converter!")
    while True:
        try:
            user_input = input("\nType 'length' to convert length, 'temperature' for temperature conversion, or 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            elif user_input.lower() == 'length':
                value = float(input("Enter the value to convert: "))
                from_unit = input("Enter the unit to convert from (meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ").lower()
                to_unit = input("Enter the unit to convert to (meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ").lower()
                converted_value = convert_length(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {converted_value} {to_unit}.")
            elif user_input.lower() == 'temperature':
                value = float(input("Enter the temperature value to convert: "))
                from_unit = input("Enter the unit to convert from (Celsius, Fahrenheit, Kelvin): ").capitalize()
                to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin): ").capitalize()
                converted_value = convert_temperature(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {converted_value} {to_unit}.")
            else:
                print("Invalid input. Please type 'length', 'temperature', or 'exit'.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
    