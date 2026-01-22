a = 10
b = 20

#If statement
if a < b :
  print("b is greater than a")
print("==========================")

#elif statement
if a>b :
  print("a is greater than b")
elif a==b :
  print("a and b are equal")
print("==========================")

#else statement
if a>b :
  print("a is greater than b")
else :
  print("a is not greater than b")
print("==========================")

#Nested if statement
if a <= b :
  if a == b :
    print("a and b are equal")
  else :
    print("a is less than b")
print("==========================")

#While loop
i = 1
while i < 6 :
  print(i)
  i += 1
print("==========================")

#For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits :
  print(fruit)
print("==========================")

#Using break statement in a loop
for i in range(10) :
  if i == 5 :
    break
  print(i)
print("==========================")

#Using continue statement in a loop
for i in range(10) :
  if i == 5 :
    continue
  print(i)
print("==========================")

#Using pass statement in a loop
for i in range(10) :
  if i == 5 :
    pass
  print(i)
print("==========================")

#using range() function in a for loop
for i in range(3, 10, 2) :
  print(i)
print("==========================")

#Using else statement with a loop
for i in range(5) :
  print(i)  
else :
  print("Loop is over")
print("==========================")

#Using nested loops
for i in range(3) :
  for j in range(3) :
    print("*", "-")
print("==========================")


# pattern
for i in range(5) :
  for j in range(i + 1) :
    print("*", end = " ") # to print star in same line
  print("") # to print in new line
print("==========================")

myVariable = "banana"
for x in myVariable:
  print(x)
print("\n==========================")

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue
    print(x)