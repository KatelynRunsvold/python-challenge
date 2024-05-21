import os
import csv


budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
output_path = os.path.join("..", "analysis", "analysis.csv")

months = 0
sum_profit_loss = 0


profit_loss = []
profit_loss_change = []

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:

        # calculate total number of months included in data
        months += 1 
       
        #the net amount of profit/losses over the entire period
        value = int(row[1])
        profit_loss.append(value) 
        sum_profit_loss += value

    #changes of profit/losses overtime and average of those change
    for i in range(1, len(profit_loss)):
        current_value = profit_loss[i]  
        previous_value = profit_loss[i - 1]  
    
        change = current_value - previous_value
        profit_loss_change.append(change)


# Calculate the average of the list
changes_sum = sum(profit_loss_change)
average = changes_sum / len(profit_loss_change)
rounded_average = round(average, 2)

# min and max of the changes
max = max(profit_loss_change)        
min = min(profit_loss_change)          




#print the data: to terminal and to text file
output = (
    "Financial Analysis\n"
    "--------------------\n"
    f"Total months: {months}\n"
    f"Total: ${sum_profit_loss}\n"
    f"Average Change: ${rounded_average}\n"
    f"Greatest Increase in Profits: ${max}\n"
    f"Greatest Decreas in Profits: ${min}\n"
)

print(output)
with open(output_path, "w") as txt_file:
    txt_file.write(output)