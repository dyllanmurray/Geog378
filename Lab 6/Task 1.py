import math

def allCities():
    for key in sorted(cities, key=lambda x: str(cities[x.label])):
        cities[key].printValues()


def cityList (cityDict):
    keyList=sorted(cityDict.keys())
    a_cities = ""
    counter=0
    for key in keyList:
        if counter>0:
            a_cities=a_cities+ ", "
            a_cities=a_cities+keyList[counter]
            counter+=1
        return a_cities

class city:
    def __init__(self, Label="n/a", Latitude=0.0, Longitude=0.0):
        self.label=Label

        if -90.0 <= Latitude <= 90.0:
            self.latitude = Latitude
        else:
            self.latitude = 0.0
            print("Not a valid latitude, please enter a value between -90 and 90")

        if -180.0 <= Longitude <= 180.0:
            self.longitude = Longitude
        else:
            self.longitude=0.0
            print("Not a valid longitutde, please enter a value between -180 and 180")

    def latlong(self): #prints out lat/long with the label
        print ("{} is at {}.") %(self.label,(self.latitude, self.longitude))

    def values(self):
        value = vars(self)
        print( self.label +  ":")
        print( " %s: %s" % item for item in value.items())

    def printDistance(self, othercity):
        """Calculate the distance between cities """
        try:
            lat1, lon1 = self.latitude, self.longitude
            lat2, lon2 = cities[othercity].latitude, cities[othercity].longitude

            # Convert the coordinates to radians (make sure it knows the inputs are float)
            lat1 = math.radians(float(lat1))
            lat2 = math.radians(float(lat2))
            lon1 = math.radians(float(lon1))
            lon2 = math.radians(float(lon2))
            # Great circle distance in radians
            d = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

            # Multiply radians by 6371km to get distance in km
            dist = 6371 * d

            # round the distance to the nearest int and convert to a string
            dist = str(int(dist))
            print("%s is %s kilometers from %s." % (self.label, dist, othercity))
        except:
            print("Sorry, the city '%s' isn't in my list. \nPlease choose from one of these cities:\n\n%s" % (
            othercity, cityList(cities)))

    def printPopChange(self, year1, year2):
        """Print the population change between two years for a city."""
        # convert the input years to the proper key names
        yr1 = 'yr' + str(year1)
        yr2 = 'yr' + str(year2)
        try:
            # get the values from the instance attributes
            popYear1 = float(getattr(self, yr1))
            popYear2 = float(getattr(self, yr2))
            # do the math
            popChange = abs(popYear1 - popYear2)
            print("%s's population change between %s and %s was %f million people." % (
            self.label, year1, year2, popChange))
        except:
            print(
                "One or both of the years you entered was invalid. We've got data at five year intervals from 1970 - 2010.")

try:

        myPath = "c:\\geog378\\lab6\\"
        # myPath="C:\\Users\\Dorn\\Documents\\GitHub\\\geog378\\lab6\\"
        myFile = "CityPop.csv"

        data = open(myPath + myFile, 'rt')
        # Read the header line and place it in headers
        headers = (data.readline()).split(',')

        cities = {}
        # Start the loop to add lines after the header to the dictionary
        for line in data:
            fields = line.split(',')
            cityindex = fields[4]  # set to value of label in table
            cities[cityindex] = {}  # add this city to the dictionary
            cities[cityindex] = City()  # create an instance in the class for this city

            index = 0
            while index < len(headers):
                """Loop through the values for this row and add them as attributes to the instance."""
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
        # printAllCities()#

        data.close

except IOError as e:
        print
        "ERROR: Unable to open file. \nPlease check the path and file settings in the script."  # file or path does not exist OR no read permissions






