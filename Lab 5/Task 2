#-----------Dyllan Murray--------#
#----------Task 2---------------#

import sys
def city_list(city_dict):
    """funtion to create a printable list of cities that appear in the CSV"""
    list_p = sorted(city_dict.keys())
    all_cities = ""
    idx = 0
    for key in list_p:
        if idx > 0:
            all_cities = all_cities + ", "
        all_cities = all_cities + list_p[idx]
        idx += 1
    return all_cities

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
				key=headers[index].strip('\n') #last part is to strip the new line character
				field=fields[index].strip('\n') #last part is to strip the new line character
				if key !='label':
					city[cityindex][key]=field
				index+=1

        data.close()
        print
        # Information Section
        print(
            "You can choose from the following cities:")
        print
        print
        print(city_list(city))
        print
        print
        # Request input from user
        inputCity = raw_input("Please enter a city: ")
        inputCity = inputCity.strip()  # remove any spaces from city input
        if inputCity not in city:
            # If the user provide s city not in the list - bail out.
            print("City data not available")
            exit()

        inputYear = raw_input("Please enter a year beteween 1970 and 2010: ")
        if 'yr' + inputYear not in city[inputCity]:
            # If the user provides an invalid year, bail out
            print("data from that year is not found")
            exit()

        if float(city[inputCity]['yr' + inputYear]) == 0.:
            #ensures that even if the date and city are in the spreadsheet but there is no data, exit the program.
            print
            print (
                "no population data from {0} in {1}. The city and year are valid but the data is missing.".format(
                    inputCity, inputYear))
            print("exit")
            exit()

        print
        print("The population in {0} in {1} was {2} million people.".format(inputCity, inputYear,
                                                                            city[inputCity]['yr' + inputYear]))

except:
    print "Unable to open file. Please check the path and file settings in the script." #file or path does not exist OR no read permissions
