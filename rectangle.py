#Brian Onieal
#Question 1

#Comparing the areas of two rectangles

lengthOne=float(input("Input length of rectangle 1: "))  #Multiplying length
widthOne=float(input("Input width of rectangle 1: "))    #times width
lengthTwo=float(input("Input length of rectangle 2: "))  #calculates the area
widthTwo=float(input("Input width of rectangle 2: "))    #of the rectangle

areaOne=lengthOne*widthOne   #Calculation of area for rectangle 1
areaTwo=lengthTwo*widthTwo   #Calculation of area for rectangle 2

if areaOne > areaTwo:
    print("Rectangle 1 is largest")     #Comparing the areas of the
elif areaTwo > areaOne:
    print("Rectangle 2 is largest")     #rectangles to see which is largest
else:
    print("They're equal")              #Rectangle areas are equal
    


