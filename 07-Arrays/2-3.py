# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements


total_food = 0
total_transport = 0
total_utilities = 0
grand_total = 0
weekly_totals = []
for week in monthly_expenses:
    total_food += week[0]
    total_transport += week[1]
    total_utilities += week[2]
    current_weeksum = week[0] + week[1] + week[2]
   
    weekly_totals.append(current_weeksum)

    grand_total += current_weeksum

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_food)
print('Transport:',total_transport)
print('Utilities:',total_utilities)
print('Week 1:',weekly_totals[0])
print('Week 2:', weekly_totals[1])
print('Week 3:',weekly_totals[2])
print('Week 4:',weekly_totals[3])
print('---------------')
print('TOTAL:',grand_total)