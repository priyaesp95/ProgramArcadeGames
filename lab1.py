#converting fahrenheit to celsius
fahrenheit_temperature = float(input("Enter the temperature in fahrenheit:"))

celsius_temperature = ( fahrenheit_temperature - 32 ) * 5 / 9

print("The celcius temperature is:",celsius_temperature,"\n")


#finding the area of a trapezoid
print("To find the area of trapezoid")
height = float(input("Enter the height of trapezoid:"))
bottom_base = float(input("Enter the length of the bottom base:"))
top_base = float(input("Enter the length of the top base:"))

area = 1 / 2 * ( bottom_base + top_base ) * height

print("Area of trapezoid is:", area,"\n")


#calculating bmi 
print("To calculate your BMI")
mass = float(input("Enter your mass in kg:"))
height = float(input("Enter your height in m:"))

bmi = mass / height ** 2

print("Your BMI is:", bmi) 