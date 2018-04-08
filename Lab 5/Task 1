#-------Dyllan Murray-------#
#------- Task 1-------------#


import os, math, sys

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
				key=headers[index].strip('') #last part is to strip the new line character
				field=fields[index].strip('') #last part is to strip the new line character
				if key !='label':
					city[cityindex][key]=field
				index+=1

		data.close()

except:
	print "ERROR: Unable to open file. Please check the path and file settings in the script." #file or path does not exist OR no read permissions

