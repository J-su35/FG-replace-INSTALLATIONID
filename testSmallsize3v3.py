# testSmallsize3v3.py
import csv

with open('DUMMY.csv') as file:    
    reader = csv.reader(file)
      
    headings = next(reader)
      
    # output list to store all rows
    DummyLists = []
    for row in reader:
        DummyLists.append(row[:])

print(DummyLists)
print(type(DummyLists))
print(DummyLists[1][0])

#--------------------Replacement Part------------------------
# read original test file
inputFile = open("testReadWriteReplace_small.txt", "rt")
# blank file for writing
output1 = open("ReplacedID.txt", "wt")

for line in inputFile:
	for check, rep in DummyLists:
		line = line.replace(check, rep)
	output1.write(line)

inputFile.close()
output1.close()

openResult = open("ReplacedID.txt", "rt")
print(openResult.read())

