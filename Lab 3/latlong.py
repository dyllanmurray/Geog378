#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dyllan Murray
#
# Created:     26/02/2018
# Copyright:   (c) Dyllan Murray 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys           #import system specific parameters


print "This program allows the user to input the latitude and longitude and then display the location of the points"


def lat():           # defines function lat as a set of conditional statements
                     #  to determine the location of the latitude value entered

  loopCount = 0           #set loopCount to 0
  while loopCount<4:      #initiate a while loop while loopCount is less than 3
    loopCount+=1          # increments loopCount by 1 each time the loop iterates
    try:
            latitude = float(input("Please enter a latitude: "))     # sets the variable latitude to the value of the input and attempts to convert the input to a float data type
            if latitude == 0:                                        # Conditional statement that displays the location of the input value if the input value equals 0
                print "That location is on the equator."

            elif latitude > 0 and latitude <= 90:                    # Conditional statement that displays the location of the input value if the input value is between 0 and 90
                print "That location is north of the equator"        # displays the location of the value entered

            elif latitude < 0 and latitude >= -90:                   # Conditional statement that displays the location of the input value if the input value is between 0 and -90
                print "That location is south of the equator"        # displays the location of the value entered

            else:                                                    # conditional statement that deals with any values outside of the range -90 to 90.
                print "That location does not have a valid latitude!"#  displays the location of the value entered
            break                                                    # exits the loop completly

    except:
            if loopCount ==4:       # once the counter variable gets to 4, exit the program

                sys.exit()        # system exit


            print "Please enter a valid number."


def longitude():                                                      # defines the function longitude as a set of conditional statements to determine the location of the latitude value entered

    loopCount=0                                                         #set loopCount to 0
    while loopCount <4:                                                  #initiate a while loop while loopCount is less than 3
        loopCount+=1                                                    # increments loopCount by 1 each time the loop iterates
        try:
            longit = float(input("Please enter a longitude: "))       # sets the variable longit to the value of the second input and attempts to convert the input to a float data type

            if longit == 0:                                           # conditional statement that the displays the location of the input value if the input value eqauls 0
                print "That location is on the prime meridian"

            elif longit > 0 and longit < 180:                         # conditional statement that the displays the location of the input value if the input value is between 0 and 180
                print "That location is east of the prime meridian"

            elif longit < 0 and longit > -180:                        # conditional statement that the displays the location of the input value if the input value is between 0 and -180
                 print "That location is west of the prime meridian"

            else:                                                     # conditional statement that deals with any values outside of the range -180 to 180
              print "That location does not have a valid longitude!"
            break                                                      # exits the loop completele
        except:
             if loopCount ==4:       # once the counter variable gets to 4, exit the program
                sys.exit()        # system exit
        print "Please enter a valid number."

lat()                                                                   # calls the latitude function
longitude()                                                             # calls the longitude function


