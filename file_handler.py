import pickle
"""
Function: save_to_text
Purpose: Save the expense list to a text file
Args:
  - expenses_list: list of dictionaries
  - filename: name of the file to save
Returns: None
"""

def save_to_file(expenses, filename):
  with open(filename,"w") as f:  
    for expense_list in expenses:
        str_expense = str(expense_list)
        f.write(str_expense)
        
"""
Function: save_to_pickle
Purpose: Save the expense list to a binary file
Args:
  - expenses: list of dictionaries
  - filename: name of the file to save
Returns: None
"""
 
def save_to_pickle(expenses,filename):   
    with open(filename,"wb") as f:
      pickle.dump(expenses, f)
      
"""
Function: load_from_pickle
Purpose: load and read the expense list which you save earlier
Args:
  - filename: name of the file to save
Returns: values
"""
      
def load_from_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
        
    
