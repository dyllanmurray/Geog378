#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dyllanv Murray
#
# Created:     26/02/2018
# Copyright:   (c) Dyllan Murray 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# This program calculates the area of a triangle.

# The description of the program will appear on the command prompt when the user

print "This program finds the area of a triangle."
print
#the shape variable is assigned string value of whatever the user enters.
shape = raw_input("Do you wish to calculate the area of a Triangle or Trapaziod?")

#conditional statement that performs specific actions based on what the user entered for the variable shape
if shape == "Triangle":

    # Height and base are variables that will accept user input from the command line. The user will be prompted to enter the height and base of the triangle
    height =input("Please enter the height of the triangle: ")
    base = input("Please enter the base length of the triangle: ")

   # The variable area is set to calculate the area of a triangle based on the user inputs for height and base
    area = 0.5 * height * base

   # The user will see the following printed on the command prompt. The height, base and area variables will be displayed.
    print "The area of a triangle with height", height, "and base", base, "is", area, "."
elif shape == "Trapazoid":
    # The trapazoid area calculation needs two bases and a hieght measurement. The following variables accept user input to generate an area of a trapazoid.
    trapbase1= input("Please enter the first base length of the trapazoid: ")
    trapbase2= input("Please enter the second base length of the trapazoid: ")
    trapheight = input("Please enter the height of the Trapazoid: ")

    #calculate the area of a trapazoid by summin of its bases, multiply the sum by the height of the trapezoid, and then divide the result by 2
    traparea = float((trapbase1+trapbase2)*trapheight) / 2
    print "The area of a trapazoid with height", trapheight, "and base", trapbase1, "and base", trapbase2, "is", traparea,"."

else: print "Unable to determine the input, please try again"




