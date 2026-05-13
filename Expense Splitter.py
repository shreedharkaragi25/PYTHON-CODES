
# Expense Splitter

expenses = [1200, 850, 1500, 950]

total_expense = sum(expenses)
average_share = total_expense / len(expenses)
highest_paid = max(expenses)

print("Total Expense:", total_expense)
print("Average Share:", average_share)
print("Highest Paid:", highest_paid)

print("\nAmount each friend should contribute equally:", average_share)

for i in range(len(expenses)):
    difference = expenses[i] - average_share
    if difference > 0:
        print("Friend", i + 1, "should receive", difference)
    elif difference < 0:
        print("Friend", i + 1, "should pay", abs(difference))
    else:
        print("Friend", i + 1, "settled up.")