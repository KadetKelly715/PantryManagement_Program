# to update git repository: got to terminal up top and click "new terminal"
# then enter -> git pull origin main (this updates the local folder first from anything new in github itself)
# then enter -> git commit -m 'Comment on changes made' 
# then enter -> git push

# PantryManagement_Program References (1) xlsx file with (3) separate worksheets to store data
## 1. Inventory
## 2. Recipes
## 3. Shopping History

import pandas as pd

# creating function for #1 Option: "Check My Inventory"
def check_inventory():
    inventory_df = pd.read_excel("PantryManager_Data.xlsx", sheet_name="Inventory")
    print(inventory_df)

# creating functions for #2 Option: "Update my inventory"
# Separate functions for adding or removing items from inventory
def update_inventory_for_meal(recipe_id):
    inventory_df = pd.read_excel('PantryManager_Data.xlsx', sheet_name='Inventory')
    recipes_df = pd.read_excel('PantryManager_Data.xlsx', sheet_name='Recipes')

    recipe = recipes_df[recipes_df['Recipe ID'] == recipe_id]

    for index, row in recipe.iterrows():
        ingredient = row['Ingredients']
        quantity_needed = row['Quantity per Ingredient']

        if ingredient in inventory_df['Iten Name'].values:
            inventory_df.loc[inventory_df['Iten Name'] == ingredient, 'Quantity'] -= quantity_needed
    
    inventory_df.to_excel('PantryManager_Data', sheet_name='Inventory', index=False)

def update_inventory_for_groceries(purchased_items):
    inventory_df = pd.read_excel('PantryManager_Data.xlsx', sheet_name='Inventory')

    for item in purchased_items:
        if item['name'] in inventory_df['Item Name'].values:

            inventory_df.loc[inventory_df['Item Name'] == item['name'], 'Quantity'] += item['quantity']
            inventory_df.loc[inventory_df['Item Name'] == item['name'], 'Price'] += item['price']
        else:
            new_row = pd.DataFrame([item])
            inventory_df = pd.concat([inventory_df, new_row], ignore_index=True)
    
    inventory_df.to_excel('PantryManager_Data.xlsx', sheet_name='Inventory', index=False)


# Creating Basic User Interface to start and work backwards. Starting with the options available for user.
while True:
    print('\nSelect an Option')
    print('1. Check my Inventory')
    print('2. Update my Inventory')
    print('3. Find a Meal')
    print('4. Get my shopping list')
    print('5. Analyze Pantry Data')
    print('6. Update a Database')
    print('7. End')

    selection_a = input('Enter your choice (1-8): ')

    #Creating path to call functions based on user input.
    if selection_a == '1':
        check_inventory()

    elif selection_a == '2':
        
        print('\nSelect an Option')
        print('1. Track a meal (remove from inventory)')
        print('2. Track a shopping trip (add to inventory)')
        print('3. End')

        selection_a2 = (input('Enter your choice (1-)'))

        if selection_a2 == '1':
            
            user_recipe_id = input('What meal did you make? (Enter Recipe ID)')
            update_inventory_for_meal(user_recipe_id)

        elif selection_a2 == '2':
            
            user_bought_groceries = input('What groceries did you buy?')
            update_inventory_for_groceries([{user_bought_groceries}])

        elif selection_a2 == '3':
            break
        else:
            print('Could not understand you chooice. Please try again.')

    elif selection_a == '3':
        pass

    elif selection_a == '4':
        pass
    elif selection_a == '5':

        pass
    elif selection_a == '6':
        pass

    elif selection_a == '7':
        break

    else:
        print('Choice not identified. Please try again')