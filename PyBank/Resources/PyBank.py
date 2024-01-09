import csv

#initiallizing all the variables to be used

#will hold all the months from imported csv
total_months = []

#will hold all data from profits/loss coloumn
balance = []

#will be used to calculate difference between months
monthly_change = []

#will be the total profit/loss over all months
net_total = 0

        
#opens the budget CSV file
with open('budget_data.csv', newline='') as f:
    reader = csv.reader(f)
    
    #skips header row
    header = next(reader)
    
    #for row in reader:
    #    print(row)
        
    for row in reader: 
        #creates list with the correct values for each row for the moths and balance columnm
        total_months.append(row[0])
        balance.append(int(row[1]))


#counts the total amount of profits/loss for the data set
for i in range(len(balance)-1):
    net_total = net_total + balance[i]

#finds the change from current month and the next month
for i in range(len(balance)-1):
    monthly_change.append(balance[i+1]-balance[i])
        
#finds the average change in the monthly amount and rounds
average_change = sum(monthly_change)/len(monthly_change)
average_change = round(average_change,2)

# Obtain the max and min of the the montly profit change list and the indexes of those. Adding 1 to account for the following month where the max/min is accounted for
greatest_inc = max(monthly_change)
inc_index = monthly_change.index(max(monthly_change))+1

greatest_dec = min(monthly_change)
dec_index = monthly_change.index(min(monthly_change))+1

#prints required information to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {total_months[inc_index]} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {total_months[dec_index]} (${greatest_dec})")

#prints to a .txt file
with open('PyBank_Results.txt', 'w') as myfile:
    print("Financial Analysis", file=myfile)
    print("----------------------------", file=myfile)
    print(f"Total Months: {len(total_months)}", file=myfile)
    print(f"Total: ${net_total}", file=myfile)
    print(f"Average Change: ${average_change}", file=myfile)
    print(f"Greatest Increase in Profits: {total_months[inc_index]} (${greatest_inc})", file=myfile)
    print(f"Greatest Decrease in Profits: {total_months[dec_index]} (${greatest_dec})", file=myfile)
myfile.close()








