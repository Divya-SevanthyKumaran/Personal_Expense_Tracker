expenses = []

valid_categories = {"Food", "Transport", "Entertainment", "Bills", "Other"}

def add_expense(expenses, expense_date, category_name, total_expense, description):
    expense = {
        "Date": (expense_date),
        "Category": category_name,
        "Amount": total_expense,
        "Description": description
    }
    if category_name not in valid_categories:
        print("Enter valid category")
    elif total_expense <= 0:
        print("The amount should be above 0")
    else:
        expenses.append(expense)
        return "Expense added successfully"

def delete_expense(expenses, expense_id):
    #if expense_id < 0 or expense_id >= len(expenses):
    if expense_id  not in range(0,len(expenses)) :  
        print("No Matching Found")
    else :
        expenses.pop(expense_id)
        return "Expense deleted successfully"
def expense_report_generator(expenses):
    for expense in expenses:
        yield expense["Amount"]
        
def save_generator(expenses):
    for expense in expenses:
       yield f"{expense['Date']}|{expense['Category']}|{expense['Amount']}|{expense['Description']}\n"
        
        
def calculate_total(expenses):
    expense_total = 0
    for line in save_generator(expenses):
        print(line, end="")
    for amt in expense_report_generator(expenses):
        expense_total += amt
        
    return expense_total
        
def filter_by_category(expenses, category_name):
    lambda_categ =filter(lambda x : x["Category"] == category_name, expenses)
    format_category = [f"{categ['Date']}:rs{categ['Amount']}-{categ['Description']}" for categ in lambda_categ]
    print(format_category)
    total_amount = 0
    for categ in expenses:
        if category_name == categ["Category"]:
           total_amount += categ["Amount"]
    print("Total : rs",total_amount)
    #total_amount = [sum(categ["Amount"]) for categ in expenses if categ["Category"] == category_name]
    #print("Total : rs", total_amount)

def get_monthly_total(expenses, Month):
    monthly_total = 0 
    for month in expenses:
        split_month = month["Date"].split("-")
        if Month == split_month[1]:
           monthly_total = monthly_total + month["Amount"]
    return monthly_total
        
def view_expense(expenses) :
    if len(expenses) == 0:
        print("No results found")
        return "The expense list is empty"
    
    for i,items in enumerate(expenses, start=0):
        print(f"{i} Date : {items['Date']} | Category : {items['Category']} | Amount : {items['Amount']} | Description : {items['Description']}")
        
