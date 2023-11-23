#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 23rd, 2023
# This program uses a function to convert from celsius to fahrenheit.
def fahrenheit():
    try:
        # Prompting the user to enter the temperature in Celsius
        temperature_celsius = float(input("Enter temperature in Celsius: "))

        # Converting the temperature from Celsius to Fahrenheit
        temperature_fahrenheit = (9 / 5) * temperature_celsius + 32

        # Displaying the converted temperature in Fahrenheit
        print(f"The temperature in Fahrenheit is: {temperature_fahrenheit}°F")
    # Response to invalid inputs
    except ValueError:
        print("Invalid input, please enter a temperature in Celsius.")


def main():
    fahrenheit()

if __name__ == "__main__":
    main()
