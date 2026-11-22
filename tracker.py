import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


while True:
    print("1. Add Expense\n2. View Expenses\n3. Show Total Expenses\n4. Exit")
    while True:
        try:
            ch=int(input("Enter your choice: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
    if ch==1:
        while True:
            try:
                amt = float(input("Enter the amount of expense: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid input.")
        while True:
            category = input("Enter the category of expense: ").strip()
            if category and not category.isdigit():
                break
            else:
                print("Category cannot be empty or a number. Please enter a valid category.")
        expenses = load_expenses()
        expenses.append({"Amount": amt, "Category": category})
        save_expenses(expenses)
        print("Expense added successfully.")
    elif ch==2:
        expenses = load_expenses()
        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(f"Amount: {expense['Amount']}, Category: {expense['Category']}")
    elif ch==3:
        expenses = load_expenses()
        if not expenses:
            print("No expenses recorded.")
        else:
            total_expense = sum(expense['Amount'] for expense in expenses)
            print(f"Total Expenses: {total_expense}")
    elif ch==4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
