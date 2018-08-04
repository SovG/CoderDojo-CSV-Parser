# Script parses in CSV data from CoderDojo Website regarding hours logged
# by Mentors over the Semester. Data needs to be of a vaild form for it to work
# 
# Created by Nehal Ghuman - 04/08/2018

import csv
import sys

def main():
	try:
		testFile = open(sys.argv[1], 'r')
		print("Test")
	except IOError as e:
		print("Please Input a Valid CSV File")
		return
	testFile.close()
	mentDict = parseFile(sys.argv[1])
	printHours(mentDict)


# Read Line, Ping Dictionary to check if User has already been created
# Add to dictionary if not, otherwise increment hours by set amount
def parseFile( filename ):
	# Create a new Dictionary
	mentorDictionary = dict()
	with open (filename) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			# Check if Mentor is Curtin Student
			if row[11] == 'Curtin University':
				studentID = int(row[13])
				# Split hours up into Useful figures
				firstHourParts = row[7].split(':')
				firstHour = float(firstHourParts[0]) + (float(firstHourParts[1]) / 60)  
				secondHourParts = row[8].split(':')
				secondHour = float(secondHourParts[0]) + (float(secondHourParts[1]) / 60)
				hours = secondHour - firstHour
				# Check if Mentor input Extra Hours
				if row[9] != '':
					thirdHourParts = row[9].split(':')
					thirdHour = float(thirdHourParts[0]) + (float(thirdHourParts[1]) / 60)
					hours += thirdHour
				# Check if Mentor has already been added to Dictionary
				if studentID in mentorDictionary:
					currMent = mentorDictionary[studentID]				
					currMent.hours += hours
					mentorDictionary[studentID] = currMent					
				# Update Hours if Mentor already found
				else:
					newMent = mentor(row[1]+" "+row[2], hours, row[13], row[5])
					mentorDictionary.update({studentID: newMent})
	return mentorDictionary

# Print out Accumulated hours to Terminal and to hours.csv file
def printHours(mentDict):
	with open('hours.csv', 'w') as outfile:
		writer = csv.writer(outfile)
		writer.writerow(['Name', 'StudentID', 'Hours', 'Role'])
		for key in mentDict:
			currMent = mentDict[key]
			print("Name: "+str(currMent.name)+". Hours: "+str(currMent.hours))
			writer.writerow([currMent.name, currMent.studentID, currMent.hours, currMent.role])

# "Data Model" for mentors 
class mentor():
	def __init__(self, name, hours, studentID, role):
		self.name = name
		self.hours = hours
		self.studentID = studentID
		self.role = role
		

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Please Input a CSV file in the CommandLine Arguments")
	else:
		main()