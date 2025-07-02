#a=2#integer
#b=3.5#flfoat
#c=a+b #adition
#d=a-b #substraction
#e=a*b #multiplication
#f=a/b #division
#print(c)
#print(d)
#print(e)
#print(f)
#print("Hello Rotislav")
#variable of type string equal to your name
#name="Juan Felipe Diaz"
#variable of type integer equal to your age
age=19
#print "my name is <name> and I am <age> years old" 
#print("My name is", name,"and I am", age, "years old")
list=["Juan", "Rotislav", "Angel", "Oriol"]
#print(list[1])
#variable of length
x=50
#variable width
y=90
#calculation of perimeter
perimeter=2*(x+y)
#calculation of area
area=x*y
#print(f"The perimeter of the rectangle is {perimeter}and the area is {area}")
numbers=[1, 2, 3, 4, 5, 8,3,5,2]
addition=sum(numbers)
#print(f"The sum of my numbers is {addition}")

length=len(numbers)
#print(f"The length of my array is {length}")

#average of the list(array)
ave=addition/length
#print(f"The average of the array is {ave}")
city_name="Barcelona"
current_temperature=33.0
#print(f"In {city_name} the current temperature is {current_temperature}")
#if current_temperature < 15:
 #   print("It's too cold")
#else:
#    print("It's too hot")
#energy=10
#for i in range(10):
#    print(i)
#while energy >= 0:
#    print(energy)
 #   energy=energy-1
 #For method
#for digit in range(2,11,2):
 #  print(digit)
#index=0
#   while index<11:
#     while index%2==0:
#     print(index)
#    index=index+1
#  index=index+1
#For while method
#o=0
#while o<11:
#    if o%2==0:
#        print(o)
#    o=o+1
#functions
a=float(input("give a number1:"))
b=float(input("give a number2:"))
def addition_func(a,b):
    return a+b
def sub_func(a,b):
    return a-b
def mult_func(a,b):
    return a*b
def div_func(a,b):
    return a/b
operator=input("give me a valid operator:")
def calculator(a,b,operator):
    if operator=='+':
        return addition_func(a,b)
    elif operator=='-':
        return sub_func(a,b)
    elif operator=='*':
        return mult_func(a,b)
    elif operator=='/':
        return div_func(a,b)
    else:
        print("Operador incorrecto")
print(calculator(a,b,operator))
