import math

def which_shape():
    # asking user what shape they want to caluctlate for. If the shape the user anwsers is not
    # a valid 2D shape in then it prints an error message then exits the program. If the shape is valid
    # the input is returned to the main area
    shape = input("Enter a 2D shape: ").lower()
    if shape == "rectangle":
        return shape
    elif shape == "triangle":
        return shape
    elif shape == "circle":
        return shape
    elif shape == "trapezoid":
        return shape
    elif shape == "hexagon":
        return shape
    else:
        print("Invalid shape entered")
        exit()

# if the user entered rectangle as their shape, this subroutine is called. The user is then asked
# for the values required in order to calculate for the area and perimeter of the shape then the
# calculation is preformed and the values are returned to the main program.
# if any of the number values the user entered is 0 or negitive then the if statement will catch it, print a error message then exit the program.
# this same concept is used for the following subroutines for the possible outcomes of 2D shapes.
def rectanlge():
    lenght = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectanlge: "))

    if width <= 0 or lenght <= 0:
        print("Invalid value entered")
        exit()

    area = width * lenght
    perimeter = (2 * width) + (2 * lenght)

    return area, perimeter

def triangle():
    base = float(input("Enter the base length: "))
    side2 = float(input("Enter the second side length of the triangle: "))
    side3 = float(input("Enter the third side length of the triangle: "))
    height = float(input("Enter the height length of the triangle: "))

    if base <= 0 or side3 <= 0 or side2 <= 0 or height <= 0:
        print("Invalid value entered")
        exit()

    perimeter = base + side3 + side2
    area = (base * height) / 2

    return area, perimeter

def circle():
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Invalid value entered")
        exit()

    perimeter = 2 * radius * math.pi
    area = math.pi * (radius**2)

    return area, perimeter

def trapezoid():
    top = float(input("Enter the top length of the trapezoid: "))
    bottom = float(input("Enter the bottom length  of the trapezoid: "))
    left_side = float(input("Enter the left side length of the trapezoid: "))
    right_side = float(input("Enter the right side length of the trapezoid: "))
    height = float(input("Enter the height length of the trapezoid: "))

    if top <= 0 or bottom <= 0 or left_side <= 0 or right_side <= 0 or height <= 0:
        print("Invalid value entered")
        exit()

    perimeter = top + bottom + left_side + right_side
    area = ((top + bottom) / 2 ) * height

    return area, perimeter

def hexagon():
    length = float(input("Enter a side length of the hexagon: "))

    if length <= 0:
        print("Invalid value entered")
        exit()

    perimeter = length * 6
    area = ((3 * math.sqrt(3)) / 2) * (length**2)

    return area, perimeter

# this calls a subroutine to get the user input of the shape
shape = which_shape()
# creating the area and perimeter varible so it can later be called
area = 0
perimeter = 0
# goes through each option of shape possible then calls the correct subroutine for the calcultions accordinly
if shape == "rectangle":
    area, perimeter = rectanlge()
if shape == "triangle":
    area, perimeter = triangle()
if shape == "circle":
    area, perimeter = circle()
if shape == "trapezoid":
    area, perimeter = trapezoid()
if shape == "hexagon":
    area, perimeter = hexagon()
# after reciving the calcutions from the subroutines it prints out a finql message telling the user the summary
print("\nShape: {0} \nPerimeter: {1: .2f} \nArea: {2: .2f} ".format(shape, perimeter, area))
