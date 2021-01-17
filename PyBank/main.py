import os
import csv

Py_Bank = os.path.join('C:\\Users\\goooo\\LearnPython\\PythonHW\\PyBank\\Resources\\PyBank_budget.csv')
money_Data = []
months = []
money_change =[]
average_change = []    

with open(Py_Bank, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    #print(csvreader)

# Print PyBank_budget
    for row in (csvreader):
        money_Data.append(int(row[1]))
        months.append(row[0])
    
    month_count = len(months)

    total = sum(money_Data)

    maxchange = money_Data[0]
    maxdate = 0
    minchange = money_Data[0]
    mindate = 0
    for row in range(1,len(money_Data)):
        change = (int(money_Data[row]) - int(money_Data[row-1]))   
        money_change.append(change)
        if change > maxchange:
            maxchange = change
            maxdate= row
        if change < minchange:
            minchange = change
            mindate = row
    average_change = sum(money_change) / len(money_change)
    
    print(f"Financial Analysis")
    print(f"-------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${'{0:.2f}'.format(average_change)}")
    print(f"Greatest Increase in Profits: {months[maxdate]} ${maxchange}")
    print(f"Greatest Decrease in Profits: {months[mindate]} ${minchange}")

    file = open("C:\\Users\\goooo\\LearnPython\\PythonHW\\PyBank\\PyBankHW.txt","w")
    file.write(f"Financial Analysis")
    file.write(f"-------------------------")
    file.write(f"Total Months: {month_count}")
    file.write(f"Total: ${total}")
    file.write(f"Average Change: ${'{0:.2f}'.format(average_change)}")
    file.write(f"Greatest Increase in Profits: {months[maxdate]} ${maxchange}")
    file.write(f"Greatest Decrease in Profits: {months[mindate]} ${minchange}")
    file.close()
