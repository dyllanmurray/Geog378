"""

Dyllan Murray
Lab 6
April 10 2018
Geog 378


"""

import math

def allCities(): #define a function to display all cities and corresponding values
    for key in sorted(cities, key=lambda x: str(cities[x].label)):
        cities[key].values()


def cityList (cityDict): #define city with the object cityDict list to read in city values from csv
    keyList=sorted(cityDict.keys())
    a_cities = ""
    counter=0
    for key in keyList:
        if counter>0:
            a_cities=a_cities+ ", "
            a_cities=a_cities+keyList[counter]
            counter+=1
        return a_cities

class city: #establish the class city
    def __init__(self, Label="n/a", Latitude=0.0, Longitude=0.0): #use of the __init__ function to to initialize the attributes the city class
        self.label=Label

        if -90.0 <= Latitude <= 90.0:  #defining the latitude
            self.latitude = Latitude
        else:
            self.latitude = 0.0
            print("Not a valid latitude, please enter a value between -90 and 90")

        if -180.0 <= Longitude <= 180.0:  #defining the longitude
            self.longitude = Longitude
        else:
            self.longitude=0.0
            print("Not a valid longitutde, please enter a value between -180 and 180")

    def latlong(self): #prints out lat/long with the label
        print ("%s is at %s.") %(self.label,(self.latitude, self.longitude))

    def values(self): #Prints the variables for an instance (in alphabetical order).
        val = vars(self)
        print self.label + ":"
        # prints the attribute name and value for all attributes for this instance
        print ' ' + '  \n'.join("%s: %s" % item for item in val.items())

    def distanceCalc(self, othercity): #Calculate the distance between cities
        try:
            lat1, lon1 = self.latitude, self.longitude
            lat2, lon2 = cities[othercity].latitude, cities[othercity].longitude

            # Convert the coordinates to radians
            lat1 = math.radians(float(lat1))
            lat2 = math.radians(float(lat2))
            lon1 = math.radians(float(lon1))
            lon2 = math.radians(float(lon2))
            # Great circle distance in radians
            d = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

            # Multiply radians by 6300km to get distance in km
            dist = 6300 * d

            # round the distance to the nearest int and convert to a string
            dist = str(int(dist))
            print("%s is %s kilometers from %s." % (self.label, dist, othercity))
        except:
            print("unable to find the city '%s'")
    def popChangeCalc(self, year1, year2):
        #Print the population change between two years for a city
        # convert the input years to the proper key names
        yr1 = 'yr' + str(year1)
        yr2 = 'yr' + str(year2)
        try:
            # get the values from the instance attributes
            year1Population = float(getattr(self, yr1))
            year2Population = float(getattr(self, yr2))
            # do the math
            popChange = abs(year1Population - year2Population)
            print("%s's population change between %s and %s was %f million people." % (
            self.label, year1, year2, popChange))
        except:
            print(
                "One or both of the years you entered was invalid.")

try:

    csvPath = "C:\Users\Dyllan Murray\Desktop\\"
    csvFile = "CityPop.csv"

    data = open(csvPath + csvFile, 'rt')
    # Read the header line and place it in headers
    headers = (data.readline()).split(',')

    cities = {}
    # Start the loop to add lines after the header to the dictionary
    for line in data:
        fields = line.split(',')
        cityindex = fields[4]  # set to value of label in table
        cities[cityindex] = {}  # add this city to the dictionary
        cities[cityindex] = city()  # create an instance in the class for this city

        index = 0
        while index < len(headers): #Loop through the values for this row and add them as attributes
            key = headers[index].strip('\n')  # last part is to strip the new line character
            field = fields[index].strip('\n')  # last part is to strip the new line character
            if index == 0:
                # first column should be an int value
                field = int(field)
            elif index in (3, 4):
                # city and label are both strings
                field = str(field)
            else:
                # everything else should be a float
                field = float(field)

            # set the attribute for each row.
            setattr(cities[cityindex], key, field)
            index += 1

    # print all the values:
    #printAllCities()#

    data.close()

except:
        print
        "ERROR: Unable to open file. "  # file or path does not exist OR no read permissions
"""
Test Scenario
The following arguments are passed through the cities class and call the specific functions

"""
cities['New York'].latlong()
#cities['Los Angeles'].distanceCalc('Beijing')
#cities['Lagos'].values()
#cities['Buenos Aires'].popChangeCalc(1995,2005)
#allCities()






