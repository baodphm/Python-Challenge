import os
import csv

Py_Roll = os.path.join('C:\\Users\\goooo\\LearnPython\\PythonHW\\Python-Challenge\\PyRoll\\Resources\\Election_Data.csv')
Voter_ID = []
County = []
Candidate = []

with open(Py_Roll, newline='') as csvfile:
    Election = csv.reader(csvfile, delimiter =',')
    header = next(Election)
#print(Election)

    for row in (Election):
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    Total_Vote = len(Voter_ID)

for row in range(1,len(Candidate)):
    
    print(f'Election Results')
    print(f'------------------------')
    print(f'Total Votes: {Total_Vote}')
    print(f'------------------------')
