def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))
def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))
def get_temperature_input():
    temp = float(input("Enter the temperature value: "))
    return temp
def get_conversion_choice():
    print("Choose the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = int(input("Enter the number of your choice: "))
    return choice
def main():
    temp = get_temperature_input()
    choice = get_conversion_choice()

    if choice == 1:
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif choice == 2:
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    elif choice == 3:
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C is {result}K")
    elif choice == 4:
        result = kelvin_to_celsius(temp)
        print(f"{temp}K is {result}°C")
    elif choice == 5:
        result = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is {result}K")
    elif choice == 6:
        result = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is {result}°F")
    else:
        print("Invalid choice. Please choose a number between 1 and 6.")
if __name__ == "__main__":
    main()
