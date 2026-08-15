import matplotlib.pyplot as plt

def set_savings_goal():
    goal = float(input("Enter your monthly savings goals:"))
    print(f"Monthly savings goals set to: ${goal:,.2f}")
    return goal

def add_income():
    income = float(input("Enter your income amount: "))
    print(f"Income of ${income:.2f} added.")
    return income

expenses = []

def add_expense():
    category = input("Enter expense category (housing, food, transport, etc): ").capitalize()
    amount = float(input("Enter expense amount: "))
    expenses.append({"category": category, "amount": amount})
    print(f"Expense of ${amount:.2f} added to {category}.")

def view_expenses_by_category():
    from collections import defaultdict
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense["category"]] += expense["amount"]
    print("\nExpenses by category:")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")     

def calculate_remaining_budget(income, expenses):
    total_expenses = sum(expense["amount"] for expense in expenses)
    remaining = income - total_expenses
    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining:.2f}")
    return remaining

def plot_expenses():
    if not expenses:
        print("No expenses to plot.")
        return
    from collections import defaultdict
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense["category"]] += expense["amount"]
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())    
    plt.figure(figsize=(8,6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expenses Distribution")
    plt.show()

def main():
    print("Welcome to the Personal Budget Planner!!")
    goal = set_savings_goal()
    income = add_income()
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses by Category")
        print("3. Calculate Remaining Budget")
        print("4. Plot Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses_by_category()
        elif choice == "3":
            calculate_remaining_budget(income, expenses)
        elif choice == "4":
            plot_expenses()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()