def add_expense(expenses, amount, category):
  if category not in expenses:
      expenses[category] = []
  expenses[category].append(amount)
  return expenses

def print_expenses(expenses):
  total = 0
  for category, amounts in expenses.items():
      total += sum(amounts)
      print(f"{category}: {sum(amounts)}")
  print(f"Total: {total}")

def main():
  expenses = {}
  while True:
      command = input("Enter expense (amount category): ")
      if command == "done":
          break
      amount, category = command.split()
      expenses = add_expense(expenses, int(amount), category)
  print_expenses(expenses)

main()