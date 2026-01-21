import math

#min() and max() functions
x = min(10,45,95,0,75)
y = max(10,45,95,0,75)
print(x)  
print(y)

#abs() function
x = abs(-7.25)
y = abs(7.25)
print(x)
print(y)

#pow() function
x = pow(4,3)
y = pow(2,5)
print(x)
print(y)

#math.sqrt() function
x = math.sqrt(64)
y = math.sqrt(81)
print(x)
print(y)

#math.ceil() and math.floor() functions
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

#math.factorial() function
x = math.factorial(5)
y = math.factorial(7)
print(x)
print(y)

#mathi.pi constant
pi = math.pi
y = math.pi * 2
print(x)

#1. Write a Python program to convert degree to radian.
deg = 15
radians = deg* (math.pi / 180)

print("radians =", radians)


# 2. Write a Python program to convert radian to degree.

rad= .52
deg = rad * (180 / math.pi)
print("degrees =", deg)

# 3. Write a Python program to calculate the area of a parallelogram.
base = 5
height = 10
area = base * height
print("Area of parallelogram ="+ str(area))


# 4. Write a Python program to calculate surface volume and area of a cylinder.
radius = 7
height = 10
volume = math.pi * radius**2 * height
surface_area = 2 * math.pi * radius * (radius + height) 
print("Volume of cylinder =" + str(volume))
print("Surface area of cylinder =" + str(surface_area))

# 5. Find the area of a Circle
radius = 5
area = math.pi * radius**2
print("Area of Circle =" + str(area))

# 6. Find the smallest value from the given List of numbers
numbers = [45, 2, 89, 15, 7, 23]
smallest = min(numbers)
print("Smallest number is =" + str(smallest))

# Find the highest value from the given List of numbers
numbers = [45, 2, 89, 15, 7, 23]
highest = max(numbers)
print("Highest number is =" + str(highest))