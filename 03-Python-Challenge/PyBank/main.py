import os
import csv


## 03-Python-Challenge\PyBank\Resources\budget_data.csv

filepath = os.path.join(".", "03-Python-Challenge", "PyBank", "Resources", "budget_data.csv")

profit = []
total = 0
count = 0
average = 0
change = []
date =[]
var = 0

with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        # Apending Profit (column 1) columnn to a list called profit
        profit.append(float(row[1]))

        # Appending date (colum 0) to a list called date
        date.append((row[0]))


        total += int(row[1])
        count = count + 1
        #average = total/count
    print("\n Financial Analysis")
    print("----------------------")
    print(f" Total Months: {count}")
    print(f" Total: ${total}")
    


# insert zero in the first row of list change(revenue change). 
# we have to do this because  the first year change in row 2 change will be no change
# so in order to get Correct index on Date we have to skip a row

    change.insert(0, var)

#Starting a new For loop for calculation of the new columns Change (monthly profit change)
    for i in range(1, len(profit)):
        change.append(profit[i] - profit[i-1])
        
        average = round(sum(change)/len(change),2)
        maxchange = max(change)
        minchange = min(change)
    ## To find Index (position of the Max change in Profit) in the Date column.
        maxdate = str(date[change.index(max(change))])
        mindate = str(date[change.index(min(change))])

    
    print(f" Average change: ${average}")
    print(f" Greatest Increase in Profits: {maxdate}  ${maxchange}")
    print(f" Greatest Decrease in Profits: {mindate}  ${minchange}\n")
   
# roster = zip(f'{total}, {count}, {average}, {maxdate}, {maxchange}, {mindate}, {minchange}')

### 03-Python-Challenge\PyBank\Resources

outputpath = os.path.join(".", "03-Python-Challenge", "PyBank", "Resources", "Analysis.csv")

with open(outputpath, 'w', newline='') as r:
    # print(roster)
    csvwriter = csv.writer(r, delimiter=',')
    ## This will Wirte the Header row
    csvwriter.writerow(['Total Profit', 'Total Month', 'Average Change in Profit', 'Date of Max Change', 'Max Change $', 'Date of Min Change', 'Min Change $'])
    ## This will Write all other Rows
    # csvwriter.writerow(f'{total} {count} {average} {maxdate} {maxchange} {mindate} {minchange}')
    csvwriter.writerow([total, count, average, maxdate, maxchange, mindate, minchange])
    
print("CSV File Updated\n")



