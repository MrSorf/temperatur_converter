
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = 9/5 * celsius + 32
    print(f"your converted celsius is {fahrenheit}\u00b0F")
    
def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"your converted fahrenheit is {celsius}\u00b0C")
    

choice = input("Please enter a temperature(C for celsius, F for fahrenheit): ").strip().upper()

if choice == 'C':
    celsius_input = float(input("Please enter temperature in celsius(\u00b0C):  "))
    convert_celsius_to_fahrenheit(celsius_input)

elif choice == 'F':
     fahrenheit_input = float(input("Please enter temperature in fahrenheit(\u00b0F):  "))
     convert_fahrenheit_to_celsius(fahrenheit_input)

else:
    print("Invalid choice, please enter 'C' or 'F'")

