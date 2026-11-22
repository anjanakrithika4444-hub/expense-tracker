# Expense Tracker

A command-line expense tracker written in Python. It lets you record what you spend, view your expenses, and see totals overall and by category. Your data is saved in a JSON file, so it's still there the next time you run the program.

## Features
- Add an expense with an amount, a category and an automatic date
- View all recorded expenses
- See the total of all expenses
- Delete an expense by choosing its number from a list
- See totals grouped by category
- Handles invalid input without crashing

## How to run
1. Install [Python 3](https://www.python.org/downloads/)
2. Download or clone this repository
3. Open a terminal in the project folder and run:

```
python tracker.py
```

## Example

1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Delete an Expense
5. Total Expense by Category
6. Exit
Enter your choice: 1
Enter the amount of expense: abc
Invalid input. Please enter a valid input.
Enter the amount of expense: 40
Enter the category of expense: 2
Category cannot be empty or a number. Please enter a valid category.
Enter the category of expense: Metro
Expense added successfully.
1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Delete an Expense
5. Total Expense by Category
6. Exit
Enter your choice: 2
Amount: 40.0, Category: Metro, Date: 2026-11-22
Amount: 150.0, Category: Travel, Date: 2026-11-22
1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Delete an Expense
5. Total Expense by Category
6. Exit
Enter your choice: 3
Total Expenses: 190.0
1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Delete an Expense
5. Total Expense by Category
6. Exit
Enter your choice: 6
Exiting the program. Goodbye!

## How it works
Each expense is stored as a dictionary with an amount, a category and a date. All expenses are kept in a list and saved to `expenses.json` using Python's `json` module. The file is loaded at the start of every action and saved after every change.

## What I learned
- Reading and writing JSON files
- Using functions to avoid repeating code
- Validating user input with `try/except`
- Working with lists, dictionaries, list of dictionaries
- Using Git and GitHub to track my work

## Planned improvements
- Filter expenses by date or month
- Export to CSV
