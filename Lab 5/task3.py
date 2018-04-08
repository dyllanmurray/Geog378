#-------Dyllan Murray------#
#------Task 3--------------#

import math

def city_list(city_dict):
    """fucntion to create a printable list of cities that appear in the CSV file """
    list_k = sorted(city_dict.keys())
    all_cities = ""
    idx = 0
    for key in list_k:
        if idx > 0:
            all_cities = all_cities + ", "
        all_cities = all_cities + list_k[idx]
        idx += 1
    return all_cities


def calc_dist(lat1, lon1, lat2, lon2):
    """Calculate the distance between two coordinates using great circle calculation."""
    # Convert the coordinates to radians (make sure it knows the inputs are float)
    lat1 = math.radians(float(lat1))
    lat2 = math.radians(float(lat2))
    lon1 = math.radians(float(lon1))
    lon2 = math.radians(float(lon2))

    # Great circle distance formula
    d = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

    # Multiply radians by 6300km to get distance in km
    dist = 6300 * d

    return dist


def inputCityScrub(string):
    string = string.strip()
    string = string.lower()
    string = string.title()
    return string

csvPath= "C:\Users\Dyllan Murray\Desktop\\"
csvFile= "CityPop.csv"

try:
	with open(csvPath + csvFile, 'rt') as file:
		data=open(csvPath + csvFile, 'rt')
		# Read the header line and place it in headers
		headers=(data.readline()).split(',')

		city={} # create city dictionary

		# Start the loop to add lines after the header to the dictionary
		for line in data:
			fields=line.split(',')
			cityindex=fields[4] #Assign the value from the field 'city' to the dictionary key
			city[cityindex]={} # add the city to the city dictionary

			index = 0
			while index<len(headers):
				key=headers[index].strip() #last part is to strip the new line character
				field=fields[index].strip() #last part is to strip the new line character
				if key !='label':
					city[cityindex][key]=field
				index+=1

		data.close()
    # Information Section
        print(
        "This program will let find the distance between two cities. You can choose from the following cities: ")
        print
        print(city_list(city))
        print
    # Request input from user
        first_city = raw_input("Please enter the first city: ")
        first_city = inputCityScrub(first_city)

        if first_city not in city:
           # If the user provide s city not in the list - bail out.
            print("data from that city is not available.")
            exit()

        print
        second_city = raw_input("please enter the second city: ")
        second_city = inputCityScrub(second_city)
        if second_city not in city:
            # If the user provide s city not in the list - bail out.
            print("Sorry, data from that city is not available.")
            exit()

        lat1, lon1 = float(city[first_city]['latitude']), float(city[first_city]['longitude'])
        lat2, lon2 = float(city[second_city]['latitude']), float(city[second_city]['longitude'])

        distance = int(round(calc_dist(lat1, lon1, lat2, lon2),
                             0))  # call calc_dist then round the value then convert to int for printing.

        print
        print("The distance from {0} to {1} is {2} km.".format(first_city, second_city, distance))

except:
	print "ERROR: Unable to open file. Please check the path and file settings in the script." #file or path does not exist OR no read permissions



