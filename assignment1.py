# SIMPLE INVENTORY MANAGEMENT SYSTEM



inventory = {}

while True:
    print("\n=== SIMPLE INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Add item")
    print("2. Update item")
    print("3. View inventory")
    print("4.Delete item")
    print("5.Exit")
    
    choice = input("Enter an option(1-5):")
    
    if choice == "1":
        item = input("Enter item name:")
        if item in inventory:
            print("Item already exists in inventory")
        else:
            quantity = int(input("Enter quantity:"))
            inventory[item]=quantity
            print(f"Item '{item}' added with quantity '{quantity}' ")
            
    elif choice == "2":
         item = input("Enter item name to update:")
         if item in inventory:
            quantity = int(input("Enter new quantity:"))
            inventory[item]=quantity
            print(f"Item '{item}' updated to quantity '{quantity}' ")
         else:
            print("Item not found in inventory")
            
    elif choice == "3":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for item, quantity in inventory.items():
                print(f"- {item}: {quantity}")
                
    elif choice == "4":
        item = input("Enter item to delete:")
        if item in inventory:
           
            if item in inventory:
                del inventory[item]
                print(f"Item '{item}' deleted.")
            else:
                print("item not found in inventory")
                
    elif choice == "5":
        print("***Exiting Inventory Management System***")
        break
    
    else:  
        print("Invalid option. Please choose a valid option.")