import csv

# write .txt file
my_report = open('budget_report.txt', mode='w') 
budget_analysis = ("/Users/brandonrogers/Desktop/Data Analyst/Projects/python-challenge/PyBank/Resources/budget_data.csv")

# open and read csv file.  creating lists for months, profit_losses, changes
with open(budget_analysis) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    months = []
    profit_losses = []
    changes = []
# iterating through each row and adding each month to months list.  Also adding profit_losses up.
    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
total_months =len(months)
net_profit_losses = sum(profit_losses)


for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]
print("Financial Analysis")
print("-----------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_losses}")
print(f"AVerage Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date}  (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output = f'average increase = {average_change:.2f}\n greatest_increase = {greatest_increase}\n greatest_increase_date ={greatest_increase_date}\n greatest_decrease = {greatest_decrease}\n greatest_decrease_date = {greatest_decrease_date}'

my_report.write(output)

    


