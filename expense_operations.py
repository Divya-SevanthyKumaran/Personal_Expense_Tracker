valid_categories = ["Food", "Travel", "Medical", "Rent", "Other"]

def add_expense(expenses, date, category, amount, description):
    if category not in valid_categories:
        return "Enter valid category"

    if amount <= 0:
        return "The amount should be above 0"

    expense = {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }

    expenses.append(expense)
    return "Expense added successfully"
