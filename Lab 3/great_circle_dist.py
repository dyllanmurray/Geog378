#-------------------------------------------------------------------------------
# Name:    d    module1
# Purpose:
#
# Author:      Dyllan Murray
#
# Created:     26/02/2018
# Copyright:   (c) Dyllan Murray 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math, sys    #import the math and system parameters

 ###### conditional block that sets the variable latitude1 equal to a float data type
   ###### and prompts users to re-enter the value if they did not enter a value that can be successfully converted into a float
print ""
counter=0                      #set loopCount to 0
while counter<3:               #initiate a while loop while loopCount is less than 3
    counter+=1                 # increments loopCount by 1 each time the loop iterates
    try:
            latitude1 = float(input("Please enter the first location's latitude: "))   # sets the variable latitude1 to the value of the input and attempts to convert the input to a float data type
            if latitude1 == 0:                                                          # Conditional statement that displays the location of the input value if the input value equals 0
                print "That location is on the equator."

            elif latitude1 > 0 and latitude1 <= 90:                                      # Conditional statement that displays the latitude1 location of the input value if the input value is between 0 and 90
                print "That location is north of the equator"

            elif latitude1 < 0 and latitude1 >= -90:                                     # Conditional statement that displays the latitude1 location of the input value if the input value is between 0 and -90
                print "That location is south of the equator"

            else:                                                                      # conditional statement that deals with any values outside of the range -90 to 90
                print "That location does not have a valid latitude!"
            break                                                                      #completly exits the loop
    except:
        if counter == 4:                                                               # protocol if a float value is not entered
            sys.exit()                                                                 #if counter = 4, exit the program

        print "Please enter a valid number."


   ###### conditional block that sets the variable longit1 equal to a float data type
   ###### and prompts users to re-enter the value if they did not enter a value that can be successfully converted into a float
counter=0
while counter<3:
    counter+=1
    try:
            longit1 = float(input("please enter the first location's longitude: "))   # sets the variable longit1 to the value of the second input and attempts to convert the input to a float data type

            if longit1 == 0:                                                           # Conditional statement that displays the location of the second input value if the input value equals 0
                print "That location is on the prime meridian"

            elif longit1 > 0 and longit1 < 180:                                        ## Conditional statement that displays the location of the second input value if the input value is between 0 and 180
                print "That location is east of the prime meridian"

            elif longit1 < 0 and longit1 > -180:                                       ## Conditional statement that displays the location of the second input value if the input value is between 0 and -180
                 print "That location is west of the prime meridian"

            else:                                                                      # conditional statement that deals with any values outside of the range -180 to 180
              print "That location does not have a valid longitude!"
            break
    except:
         if counter == 4:                                                               # protocol if a float value is not entered
            sys.exit()
            print "Please enter a valid number."





###### conditional block that sets the variable latitude2 equal to a float data type
   ###### and prompts users to re-enter the value if they did not enter a value that can be successfully converted into a float
counter=0
while counter<3:
    counter+=1
    try:
            latitude2 = float(input("Please enter the second location's latitude: "))
            if latitude2 == 0:
                print "That location is on the equator."

            elif latitude2 > 0 and latitude2 <= 90:
                print "That location is north of the equator"

            elif latitude2 < 0 and latitude2 >= -90:
                print "That location is south of the equator"

            else:
                print "That location does not have a valid latitude!"
            break
    except:
         if counter == 4:                                                               # protocol if a float value is not entered
            sys.exit()
            print "Please enter a valid number."

   ###### conditional block that sets the variable longit2 equal to a float data type
   ###### and prompts users to re-enter the value if they did not enter a value that can be successfully converted into a float
counter=0
while counter<3:
    counter+=1
    try:
            longit2 = float(input("Please enter a longitude: "))

            if longit2 == 0:
                print "That location is on the prime meridian"

            elif longit2 > 0 and longit2 < 180:
                print "That location is east of the prime meridian"

            elif longit2 < 0 and longit2 > -180:
                 print "That location is west of the prime meridian"

            else:
              print "That location does not have a valid longitude!"
            break
    except:
         if counter == 4:                                                               # protocol if a float value is not entered
            sys.exit()
            print "Please enter a valid number."


lat1 = math.radians(latitude1)      #convert the value of latitude1 from degrees into radians
long1= math.radians(longit1)        #convert the value of longit1 from degrees into radians
lat2=math.radians(latitude2)        #convert the value of latitude2 from degrees into radians
long2=math.radians(longit2)         #convert the value of longit2 from degrees into radians

#great circle distance formula used to calculate the distance between the locations entered.
d = math.acos((math.sin(lat1)*math.sin(lat2))+(math.cos(lat1)*math.cos(lat2)*math.cos((long1)-(long2))))*6300
print 'The distance between location 1 and location 2 is:', d, 'km'
