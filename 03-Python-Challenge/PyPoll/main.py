import os
import csv

##  03-Python-Challenge\PyPoll\Resources\election_data.csv    

filepath = os.path.join(".", "PyPoll", "Resources", "election_data.csv")

candidate = []
groupcandidate = []
totalcount = 0
khan_count = 0
corry_count = 0
li_count = 0
tooley_count = 0

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # Skips header
    for row in csvreader:
        candidate.append(row[2])
        totalcount = totalcount + 1

        if row[2] == "Khan":
            khan_count = khan_count + 1
            khan_percent = khan_count/totalcount*100
        
        if row[2] == "Correy":
            corry_count = corry_count + 1
            corry_percent = corry_count/totalcount*100

        if row[2] == "Li":
            li_count = li_count + 1
            li_percent = li_count/totalcount*100
        
        if row[2] =="O'Tooley":
            tooley_count = tooley_count + 1
            tooley_percent = tooley_count/totalcount*100
    
            winner = max([khan_count, corry_count, li_count, tooley_count])

    print(" \nElection Results")
    print("----------------------------")     
    print(f'Total Votes: {totalcount}')
    print("----------------------------")   
    print(f"Khan    : {khan_percent:0.2f}%  ({khan_count})") 
    print(f"corry   : {corry_percent:0.2f}%  ({corry_count})")
    print(f"Li      : {li_percent:0.2f}%  ({li_count})")
    print(f"O'Tooley:  {tooley_percent:0.2}%  ({tooley_count})")
    print("----------------------------")
    print(f"WInner: Khan votes {winner}")
    print("----------------------------\n")


#### Write the data in CSV File.
### 03-Python-Challenge\PyBank\Resources

outputpath = os.path.join(".", "PyPoll", "Resources", "Analysis.csv")

with open(outputpath, 'w', newline='') as r:
    # print(roster)
    csvwriter = csv.writer(r, delimiter=',')
    ## This will Wirte the Header row
    csvwriter.writerow(['Total Votes', 'Khan Percent', 'Khan Total Votes', 'Corry Percent', 'Corry Total Votes', 'Li Percent', 'Li Total Votes', 'Tooley Percent', 'Tooley Total Votes'])
    ## This will Write all other Rows
    # csvwriter.writerow(f'{total} {count} {average} {maxdate} {maxchange} {mindate} {minchange}')
    csvwriter.writerow([totalcount, khan_percent, khan_count, corry_percent, corry_count, li_percent, li_count, tooley_percent,tooley_count])
    
print("CSV File Updated\n")

