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
    print("1. Add Expense\n2. View Expenses\n3. Show Total Expenses\n4. Delete an Expense\n5. Total Expense by Category\n6. Exit")
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
            category = input("Enter the category of expense: ").strip().title()
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
        expenses=load_expenses()
        if not expenses:
            print("No expenses recorded.")
        else:
            for x,expense in enumerate(expenses, 1):
                print(f'{x}. Amount: {expense["Amount"]}, Category: {expense["Category"]}')
            while True:
                try:
                    index=int(input("Enter expense index to be deleted: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number as index.")
                else:
                    if 1 <= index <= len(expenses):
                        del expenses[index-1]
                        save_expenses(expenses)
                        print("Expense deleted successfully.")
                        break
                    else:
                        print("Invalid index. Please enter a valid index.")
    elif ch==5:
        expenses = load_expenses()
        expenserev={}
        for expense in expenses:
            category = expense["Category"].title()
            amount = expense["Amount"]
            if category not in expenserev:
                expenserev[category]=[]
            expenserev[category].append(amount)
        if not expenserev:
            print("No expenses recorded.")
        else:
            for category, amounts in expenserev.items():
                total_cat_expense = sum(amounts)
                print(f"Total expense for {category}: {total_cat_expense}")
    elif ch==6:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
