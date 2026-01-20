print ("Hello, nyn!")

# Variables and Datatypes
name = "Nayan"
age = 23
is_coding = True
print(f"my name is { name } and my age is      {age}" )
print("nayan")
print("is coding")

# Input and Outputs
name = input("Enter your name: ")
print("Hello, " + name + "!")

#Operators in python
a = 10
b = 5

# Arithmetic Operators
print("Addition:", a + b)       #15
print("Subtraction:", a - b)    #5
print("Multiplication:", a * b) #50
print("Division:", a / b)       #2.0

# Comparison Operators
print("Equal:", a == b)         #False
print("Not Equal:", a != b)     #True
print("Greater than:", a > b)   #True
print("Less than:", a < b)      #False
print("Greater than or equal to:", a >= b)    #True
print("Less than or equal to:", a <= b)   #False

# Logical Operators
print("AND:", a > 5 and b < 10) #True 
print("OR:", a > 15 or b < 10)  #True
print("NOT:", not(a > 5))       #False

#assignment Operators
c = 10
c += 5
print("c after += 5:", c)     #15
c -= 3
print("c after -= 3:", c)     #12
c *= 2
print("c after *= 2:", c)     #24
c /= 4
print("c after /= 4:", c)     #6.0
c %= 3
print("c after %= 3:", c)     #0.0
c **= 2
print("c after **= 2:", c)    #0.0
c //= 2
print("c after //= 2:", c)    #0.0

#bitwise Operators
x = 6  # In binary: 110
y = 3  # In binary: 011
print("Bitwise AND:", x & y)    #2
print("Bitwise OR:", x | y)     #7
print("Bitwise XOR:", x ^ y)    #5
print("Bitwise NOT:", ~x)       #-7
print("Left Shift:", x << 1)    #12
print("Right Shift:", x >> 1)   #3


#Question 01
# Create a variable named myName and assign your name to it and display your name as follow
# eg:- My name is Jhon
myName = 'Nayan'
print("my name is " + myName)

# Question 02
# Create a variable named x and assign the value 50 to it and display it as follows
# eg:- 50 is a number
x = 50
print("eg:- " + str(x) + " is a number")
print(x)

# Question 03
# Display the sum of 5 + 10, using two variables: x and y
# eg:- The sum of 5 and 10 is equal to 15
a =5
b=10 
print("the sum of " + str(a) + " and " + str(b) + " is " + str(a+b))