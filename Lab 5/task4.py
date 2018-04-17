# ------Dyllan Murray------#
# ------Task 4 -----------#

import sys, math, os


def list_k_nest(dict_a):
    for key in dict_a.keys():
        nestedKeys = dict_a[key].keys()
        return nestedKeys


csvPath = "C:\Users\Dyllan Murray\Desktop\\"
csvFile = "CityPop.csv"

try:
    with open(csvPath + csvFile, 'rt') as file:
        data = open(csvPath + csvFile, 'rt')
        # Read the header line and place it in headers
        headers = (data.readline()).split(',')

        city = {}  # create city dictionary

        # Start the loop to add lines after the header to the dictionary
        for line in data:
            fields = line.split(',')
            cityindex = fields[4]  # Assign the value from the field city to the dictionary key
            city[cityindex] = {}  # add the city to the city dictionary

            index = 0
            while index < len(headers):
                key = headers[index].strip()  # last part is to strip the new line character
                field = fields[index].strip()  # last part is to strip the new line character
                if key != 'label':
                    city[cityindex][key] = field
                index += 1

        data.close()

except:
    print "Unable to open file. check the path and file settings in the script."  # file or path does not exist OR no read permissions
    exit()

print sorted(city, key=lambda x: (city[x]['id']))

""" Program imports the CSV file, then allows the user to select a city and year to retrieve data.
"""
# Information Section
print("This program will compare population change for cities in user defined years.")
print
print("Available years 1970 through 2010.")
print

# Request input from user
first_year = raw_input("Please enter the frist year: ")
if 'yr' + first_year not in list_k_nest(city):
    # exit If the user provides an invalid year
    print("data from that year is not available")
    exit()

# Verify there's good data from this year
# valid_pop(city,my_city,'yr'+first_year)

second_year = raw_input("Please enter the second year: ")
if 'yr' + second_year not in list_k_nest(city):
    # If the user provides an invalid year, bail out
    print("data from that year is not available")
    exit()

try:  # Try to write the data to a file.
    out = open(csvFile + "CityPopChg.csv", "wt")
    columnHeads = "id, city, population_change"
    # Write the column headings
    out.write(columnHeads)

    # Compile the data to write - grab the original ID-get the city name
    #     and the string version of the population change.

    row = ""  # Create an empty string to use in the For Loop

    # The sorted section puts it in id order
    for key in sorted(city, key=lambda x: int(city[x]['id'])):

        # Accounts for user entering the second year first
        if int(first_year) > int(second_year):
            # Calculate the population change
            pop_change = float(city[key]['yr' + first_year]) - float(city[key]['yr' + second_year])
        else:
            # Calculate the population change
            pop_change = float(city[key]['yr' + second_year]) - float(city[key]['yr' + first_year])

        # Add the data to a string that we'll write to the new file
        row = row + city[key]['id'] + ", " + city[key]['city'] + ", " + str(pop_change)
    # Write the data to the new file.
    out.write(row)

    out.close()
    print
    print("The file CityPopChg.csv was created")

except:
    print()
    print(
        "Unable to edit or save the file.")  # file or path does not exist OR no read permissions
    exit()
