from . import Expense
import collections
import matplotlib.pyplot as plt

# Create new expenses object
expenses = Expense.Expenses()

# Read in the spending data
expenses.read_expenses('data/spending_data.csv')

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

# Test printing of spending_counter
print(spending_counter)

top5 = spending_counter.most_common(5)

print(top5)

categories, count= zip(*top5)

print(f'List1 {categories}')
print(f'List2 {count}')


fig, ax = plt.subplots()
ax.bar(categories,count)
ax.set_title('# of Purchases by Category')

plt.show()