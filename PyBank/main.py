import csv
import os

file_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')
output_dir = os.path.join('PyBank', 'Analysis')
output_file_path = os.path.join(output_dir, 'financial_analysis.txt')

total_months = 0
total = 0
previous_profit_losses = None
changes = []
dates = []
greatest_increase = {"date" : None, "amount" : float("-inf")}
greatest_decrease = {"date" : None, "amount" : float("inf")}

with open (file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        date = row['Date']
        profit_losses = int(row['Profit/Losses'])

        total_months += 1
        total += profit_losses

        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            dates.append(date)

            if change > greatest_increase["amount"]:
                greatest_increase = {"date": date, "amount": change}

            if change < greatest_decrease["amount"]:
                greatest_decrease = {"date": date, "amount": change}

        previous_profit_losses = profit_losses

average_change = sum(changes) / len(changes) if changes else 0

results = {
    'Total Months': total_months,
    'Total': total,
    'Average Change': average_change,
    'Greatest Increase in Profits': (greatest_increase["date"], greatest_increase["amount"]),
    'Greatest Decrease in Profits': (greatest_decrease["date"], greatest_decrease["amount"])
}

for key, value in results.items():
    print(f"{key}: {value}")


output_dir = r'PyBank\Analysis'  

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file_path = os.path.join(output_dir, 'financial_analysis.txt')

with open(output_file_path, mode='w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Average Change: {average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['date']}, (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']}, (${greatest_decrease['amount']})\n")