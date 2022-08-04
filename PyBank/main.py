#Modules
import csv
import os

#Reading CSV Module
budget_data = os.path.join('Resources/budget_data.csv')
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the hedaer row first
    header = next(csvreader)

    #CHECK: SKIP HEADER
    #print(header)

    #List preparation
    months = []
    profit_losses = []
    changes = []

    #Task No.1: The total number of months included in the dataset
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(row[1])

    total_months = len(months)

    #CHECK: TOTAL MONTH
    #print(total_months)

    total = 0

    #Task No.2: The net total amount of "Profit/Losses" over the entire period    
    for amount in profit_losses:
        total = total + int(amount)

    #CHECK: TOTAL PROFIT/LOSS
    #print(total)

    #Task No.3: The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(total_months-1):
        change = int(profit_losses[i+1])-int(profit_losses[i])
        changes.append(change)

    #CHECK:CHANGE IN PROLOSS
    #print(changes)

    total_changes = 0

    for avg_change in changes:
        total_changes = total_changes + int(avg_change)

    final_changes = round(total_changes/(total_months-1), 2)
    
    #CHECK: AVERAGE CHANGE
    #print(final_changes)

    g_increase = 0
    g_months = ''

    #Task No.4: The greatest increase in profits (date and amount) over the entire period
    for j in range(total_months-1):
        if changes[j] > g_increase:
            g_increase = changes[j]
            g_months = months[j+1]
            
    #CHECK: MONTH + GREATEST INCREASE IN PROFITS
    #print(g_months)
    #print(g_increase)

    g_decrease = 0
    d_months = ''

    #Task No.5: The greatest decrease in profits (date and amount) over the entire period
    for j in range(total_months-1):
        if changes[j] < g_decrease:
            g_decrease = changes[j]
            d_months = months[j+1]
    
    #CHECK: MONTH + GREATEST DECREASE IN PROFITS
    #print(d_months)
    #print(g_decrease)

    #TEXT FILE
    output_file=open("Analysis/pybank.txt","w")
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write("Total Months: "+ str(total_months)+"\n")
    output_file.write("Total: $"+str(total)+"\n")
    output_file.write("Average Change: $"+str(final_changes)+"\n")
    output_file.write("Greatest Increase in Profits: "+str(g_months)+" ($"+str(g_increase)+")\n")
    output_file.write("Greatest Decrease in Profits: "+str(d_months)+" ($"+str(g_decrease)+")\n")
    output_file.close()

    #PRINT TO THE TERMINAL
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+ str(total_months)+"")
    print("Total: $"+str(total)+"")
    print("Average Change: $"+str(final_changes)+"")
    print("Greatest Increase in Profits: "+str(g_months)+" ($"+str(g_increase)+")")
    print("Greatest Decrease in Profits: "+str(d_months)+" ($"+str(g_decrease)+")")
