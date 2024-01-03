# to update git repository: got to terminal up top and click "new terminal"
# then enter -> git pull origin main (this updates the local folder first from anything new in github itself)
# then enter -> git commit -m 'Comment on changes made' 
# then enter -> git push

# PantryManagement_Program References (3) CSV files to store data
## 1. groceries.csv
## 2. pantry_items.csv
## 3. recipes.csv

import pandas as pd


# Creating Basic User Interface to start and work backwards. Starting with the options available for user.
while True:
    print('\nSelect an Option')
    print('1. Check my Inventory')
    print('2. Update my Inventory')
    print('3. Plan today\'s Meal')
    print('4. Get my shopping list')
    print('5. Analyze Pantry Data')
    print('6. Add a New Grocery Item')
    print('7. Add a New Recipe')
    print('8. End')

selection_a = input('Enter your choice (1-8): ')

#Creating shells to call functions based on user input. Functions to be added once created
if selection_a == '1':
    pass
elif selection_a == '2':
    pass
elif selection_a == '3':
    pass
elif selection_a == '4':
    pass
elif selection_a == '5':
    pass
elif selection_a == '6':
    pass
elif selection_a == '7':
    pass
elif selection_a == '8':
    break