#ask input for expense details

import expense_operations as ops
import file_handler as fh
import sys

#load expensel list from pickle file

try :
    expenses = fh.load_from_pickle("expenses.pkl")
    print(expenses)
except FileNotFoundError:
    expenses =[]
    
if not expenses:
    print("No Expenses found\n")

while True:     
    print("=====Personal Expense Tracker=====\n")
    print(f"1.Add Expense \n2.View All Expenses \n3.View by Category \n4.Monthly Summary \n5.Delete Expenses \n6.Generate Report \n7.Exit")

  
    choice = int(input("Enter your choice : "))

    if choice == 1:
         expense_date = input("Enter the date :")
         category_name = input("Enter the category : ")
         total_expense = float(input("Enter the total expense amount : "))
         description = input("Enter the description : ")
         print(ops.add_expense(expenses, expense_date, category_name, total_expense, description))
         fh.save_to_file(expenses, "expenses.txt")
         fh.save_to_pickle(expenses, "expenses.pkl")

    elif choice == 2:
         ops.view_expense(expenses)
         
    elif choice == 3:
         category_name = input("Enter the category name : ")
         ops.filter_by_category(expenses, category_name)
         
    elif choice == 4:
         Month = input("Enter the month number : ")
         print(ops.get_monthly_total(expenses, Month))
         
    elif choice == 5:
         expense_id = int(input("Enter expense id : "))
         ops.delete_expense(expenses, expense_id)
         fh.save_to_pickle(expenses, "expenses.pkl")
         fh.save_to_file(expenses, "expenses.txt")
         
    elif choice == 6:
         #print(ops.save_generator(expenses))
         print(ops.calculate_total(expenses))
         
    else :
         break
        
        


    



