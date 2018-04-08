#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dyllan Murray
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


loopCount = 0           #set loopCount to 0
while loopCount<3:      #initiate a while loop while loopCount is less than 3
    loopCount+=1        # increments loopCount by 1 each time the loop iterates
    try:
        #conditional block statement which looks to see if the user wishes to determine the area of a triangle or a trapazoid.
        if shape == "Triangle":
            height =float(input("Please enter the height of the triangle: "))                       #attempts to convert the user input for height into a float datatype
            print '\nyour input is',height, 'which has a type of',type(height)                      #prints the user input and the type

            base =float(input("Please enter the base of the triangle: "))                           #attempts to convert the user input for base into a float datatype
            print '\nyour input is',base, 'which has a type of',type(base)                          #prints the user input and the type

            area = .50* height*base                                                                 #calculates the area of a triangle using the user inputs for base and height
            print "The area of a triangle with height", height, "and base", base, "is", area, "."   #prints the area of the triangle and the user defined inputs
        break                                                                                       #breaks the loop
    except:
            print '\nyou entered a string value that can NOT be converted to an int or float value' # error message displayed when 4 attempts at entering a float have failed.

loopCount = 0           #set loopCount to 0
while loopCount<3:      #initiate a while loop while loopCount is less than 3
    loopCount+=1        # increments loopCount by 1 each time the loop iterates
    try:
        if shape == "Trapazoid":
            # The trapazoid area calculation needs two bases and a hieght measurement. The following variables accept user input to generate an area of a trapazoid.
            trapbase1= float(input("Please enter the first base length of the trapazoid: "))        #attempts to convert the user input for base1 into a float datatype
            print '\nyour input is',trapbase1, 'which has a type of',type(trapbase1)                #prints the user input and the type

            trapbase2= float(input("Please enter the second base length of the trapazoid: "))       #attempts to convert the user input for base2 into a float datatype
            print '\nyour input is',trapbase2, 'which has a type of',type(trapbase2)                #prints the user input and the type

            trapheight = float(input("Please enter the height of the Trapazoid: "))                 #attempts to convert the user input for height into a float datatype
            print '\nyour input is',trapheight, 'which has a type of',type(trapheight)              #prints the user input and the type

            #calculate the area of a trapazoid by summin of its bases, multiply the sum by the height of the trapezoid, and then divide the result by 2
            traparea = float((trapbase1+trapbase2)*trapheight) / 2
            print "The area of a trapazoid with height", trapheight, "and base", trapbase1, "and base", trapbase2, "is", traparea,"."     #displays the area of the trapazoid and the user inputs
        break                                                                                        #breaks the loop
    except:
            print '\nyou entered a string value that can NOT be converted to an int or float value' # error message displayed when 4 attempts at entering a float have failed

