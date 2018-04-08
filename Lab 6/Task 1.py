import math

def allCities():
    for key in sorted(cities. key=lambda x: str(cities[x.label])):
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




