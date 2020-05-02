
import os
import csv

csvpath = os.path.join("..", "PyBank","Resources", "budget_data.csv")

total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change = 0
total_month_change = 0
average_month_change = 0
largest_increase = 0
largest_increase_month = ""
largest_decrease = 0
largest_increase_month = ""


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
    csv_header = next(csvreader)
    
   
    for row in csvreader:
        
        total_months += 1
        
        
        total_profit_loss += int(row[1])
        
        
        if total_months > 1:
            month_change = int(row[1]) - prev_profit_loss
            
        
        total_month_change += month_change
        
        
        prev_profit_loss = int(row[1])
        
       
        if month_change > largest_increase:
            largest_increase = month_change
            largest_increase_month = row[0]
        
        
        if month_change < largest_decrease:
            largest_decrease = month_change
            largest_decrease_month = row[0]

        
average_month_change = total_month_change / (total_months - 1)

print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(format(average_month_change, '.2f')))
print("largest Increase in Profits: " + largest_increase_month 
      + " ($" + str(largest_increase) + ")")
print("largest Decrease in Profits: " + largest_decrease_month 
      + " ($" + str(largest_decrease) + ")")


