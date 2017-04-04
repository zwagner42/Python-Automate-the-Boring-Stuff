#Program to display a fantasy inventory

#Display the inventory
#inventory is a dictionary containing the contents of a player's inventory
def display_Inventory(inventory):
	print("\nInventory:")
	total_Item_Count = 0
	
	for item, amount in inventory.items():
		print(str(amount) + ' ' + str(item))
		total_Item_Count += amount
	
	if(total_Item_Count == 0):
		print("No items in your inventory!")
	print("Total numer of items: " + str(total_Item_Count))
	
#Adding items to an inventory
#inventory is a dictionary containing the contents of a player's inventory
#addedItems is a list containing the items being added to the player's inventory
def add_To_Inventory(inventory, addedItems):
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	
basic_Inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_Inventory(basic_Inventory)

goblin_Loot = ['gold coin', 'gold coin', 'dagger']

add_To_Inventory(basic_Inventory, goblin_Loot)
display_Inventory(basic_Inventory)
