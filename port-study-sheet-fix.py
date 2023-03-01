#userInput = input("File name: ")
#inputFile = open(userInput)
import re
inputFile = open('Ports-List.txt')
joinedList = list()
for line in inputFile:
	if " - " in line:
		segment = line.split()
		segment[0], segment[2] = segment[2], segment[0]
		seglen = len(segment[0])
		for addspaces in range(12-seglen):
			segment[0] = segment[0] + " "
		segment[1] = segment[1] + "   "
		joined = ' '.join(segment)
		joinedList.append(joined)

for i in range(0,len(joinedList)):
	x = re.findall('^[0-9]*', joinedList[i])
	a = int(x[0])
	for j in range(i+1):
		y = re.findall('^[0-9]*', joinedList[j])
		b = int(y[0])
		if (a < b):
			joinedList[i],joinedList[j] = joinedList[j],joinedList[i]

joinFile = open('ports-study-sheet.txt', "w")
joinFile.write("Ports Study List\n----------------\n")
for entry in joinedList:
	joinFile.write(entry)
	joinFile.write("\n")
joinFile.close()

